# -*- coding: cp936 -*-

import re
import AttendDataProcessor
import Common, Profile
from Global import *
from CFG.Standard_Table_CFG import *
from ExcelApi import XlrdExcel

def employ_id_competion(raw_id):
        id_len = 6
        raw_id = str(raw_id)
        raw_id_len = len(raw_id)
        if raw_id_len < id_len:
            while( len(raw_id) < id_len ):
                raw_id = "0%s"%raw_id
        return raw_id

class RecordSheet(XlrdExcel.XlrdExcel):
    def __init__(self):
        super(RecordSheet, self).__init__(attend_workbook_name)
        if self.load_workbook() is False: 
            self.is_open = False
            return
        else:
            self.is_open = True
        self.open_sheet(record_sheet_name)
        self.timestamp = self.get_timestamp()
        self.attend_days = self.columns
        self.start_date = Common.timestamp_to_date(self.timestamp)
        self.attend_processor = AttendDataProcessor.AttendTimeProcess(self.start_date)
        self.attend_record_info = {}
        self.__init_attend_record_info()

        
    def get_timestamp(self):
        #date = excel.get_cell_value(self.__sheet, date_row_record_sheet, date_col_record_sheet)
        date = self.get_cell_value(date_row_record_sheet, date_col_record_sheet)
        dl = re.split(r'\s+\~\s+', date)
        if len(dl): 
            d = dl[0]
            if re.search(r'\d+\-\d+\-\d+', d):
                return Common.date_to_timestamp(d)
        return float(0)
    
    # 将考勤时间字符串转换成列表
    # 08:2516:0618:04 ==> ['08:25', '16:06', '18:04']
    def attend_time_to_list(self, raw_time):
        reg_time = re.split(r"(\d{2}\:\d{2})", raw_time)
        time_list = []
        if len(reg_time):
            for t in reg_time:
                if t == '': continue
                time_list.append(t)
        return time_list
    
    def get_attend_state(self, attend_time_list):
        """
                        输入考勤时间列表
                       由打卡时间分析出出勤状态
        """
        num = len(attend_time_list)
        leave_time = ""
        if num > 1:
            leave_time = attend_time_list[num - 1]
        elif num < 1:
            return ONE_ATTEND_RECORD
        return self.attend_processor.get_attend_state(attend_time_list[0], leave_time)

    
    def __init_attend_record_info(self):
        rows_in_sheet = self.rows
        cols_in_sheet = self.columns
        row = start_empolyee_row_record_sheet
        create_year = Common.get_year_from_timestamp(self.timestamp)
        create_month = Common.get_month_from_timestamp(self.timestamp)
        # read holidays from profile
        holidays = Profile.Profile().holidays
        while(row < rows_in_sheet):
            _id = self.get_cell_value(row, id_col_record_sheet)
            _id = employ_id_competion(Common.unicode_to_int(_id))
            # 处理每个员工的考勤情况
            row += 1
            attend_info = {}
            for col in range(cols_in_sheet):
                day = int(col + 1)
                attend_time_state = UNKONW_ATTEND_STATE
                curr_tm = Common.date_to_timestamp("%s-%s-%s"%(create_year, create_month, day))
                
                # 检查该日是否为法定假日或调休日
                if len(holidays):
                    if day in holidays:
                        attend_info.update( { day: NORMAL_DAYOFF } )
                        continue
                
                # 检查该日是否为双休日
                if not Common.is_working_day(curr_tm): 
                    attend_info.update( { day: NORMAL_DAYOFF } )
                    continue
                
                attend_time = self.get_cell_value(row, col)
                
                # 非双休日时，该cell没有考勤时间，即记为缺勤
                if attend_time == '':
                    attend_info.update( { day: NO_ATTEND_RECORD } )
                    continue
                
                attend_time = Common.unicode_to_str(attend_time)
                attend_time_list = self.attend_time_to_list(attend_time)
                attend_time_state = self.get_attend_state(attend_time_list)
                attend_info.update( { day: attend_time_state } )
                
            row += 1
            self.attend_record_info.update({ _id: attend_info })
            
        
        


class SummarySheet(XlrdExcel.XlrdExcel):
    def __init__(self):
        super(SummarySheet, self).__init__(attend_workbook_name)
        if self.load_workbook() is False: 
            self.is_open = False
            return
        else:
            self.is_open = True
        self.open_sheet(summary_sheet_name)
        self.employee_base_info   = {}
        self.__init_employee_base_info()
        self.standard_attend_hours   = self.get_standard_attend_hours()
        self.standard_attend_days = self.get_standard_attend_days()
        self.employee_num = len(self.employee_base_info)
        self.timestamp = self.get_timestamp()
        self.summary_month = Common.get_month_from_timestamp(self.timestamp)
        
    def get_standard_attend_days(self):
        days = self.get_cell_value( start_empolyee_row_summary_sheet, \
                                    stand_attend_days_col_summary_sheet)
        return Common.unicode_to_str(days).split("/")[0]
    
    def get_standard_attend_hours(self):
        hours = self.get_cell_value(start_empolyee_row_summary_sheet, \
                                    stand_attend_hours_col_summary_sheet)
        return Common.unicode_to_str(hours).split(":")[0]
    
    def get_timestamp(self):
        date = self.get_cell_value(date_row_summary_sheet, date_col_summary_sheet)
        dl = re.split(r'\s+\~\s+', date)
        if len(dl): 
            d = dl[0]
            if re.search(r'\d+\-\d+\-\d+', d):
                return Common.date_to_timestamp(d)
        return float(0)
        
    
    def __init_employee_base_info(self):
        i = 1
        for row in range(self.rows - start_empolyee_row_summary_sheet):
            row += start_empolyee_row_summary_sheet
            
            employ_id = Common.unicode_to_int( self.get_cell_value(row, id_col_summary_sheet) )
            employ_id = employ_id_competion(employ_id)
            name   = self.get_cell_value(row, name_col_summary_sheet)
            depart = self.get_cell_value(row, department_col_summary_sheet)
            absent = self.get_cell_value(row, absent_col_summary_sheet)
            
            self.employee_base_info.update( {i:  {"id":        employ_id,   \
                                                  "name":       name,        \
                                                  "department": depart,      \
                                                  "absent":     int(absent), \
                                            }} )
            i += 1







    
    
    
