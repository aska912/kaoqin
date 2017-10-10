# -*- coding: cp936 -*-

import sys, re
import AttendWorkbook, Profile
import Common
from ExcelApi import OpenPyExcel
from Global import *
from CFG.Kaoqin_Check_CFG import *
from CFG.Meal_Allowance_CFG import *



class kaoqin():
    def __init__(self):
        self.workbook_name = ""
        self.sheet_name = ""
        self.year = 0
        self.month = 0
        self._workbook = None
        self._worksheet = None
        self._summary_wb = None
        self._record_wb = None
        self.holidays = []
        
        self._init_by_self()
        
    def _init_by_self(self):
        self._load_summary_sheet()
        self._load_record_sheet()
        
        self.workbook_name = attend_check_workbook_name
        self.year = Common.get_current_year()
        self.month = int(self._summary_wb.summary_month)
        self.sheet_name = ("%s%s"%(self.month, u'月'))
        
    def Create(self):
        if not self._open_excel(): return False
        if not self._add_sheet():  return False
        if not self._open_sheet(): return False

        self._write_table_header()
        self._write_check_data()
        self._close_excel(save=True)
        
    def Fanbu(self):
        if not self._open_excel(): return False
        if not self._open_sheet(): return False
        
        if self._check_adjust_data_format():
            adjust_data_dict = self._read_adjust_data()
            fanbu(self.year, self.month, adjust_data_dict).Create()
        self._close_excel()
        
    def _read_adjust_data(self):
        adjust_data = {}
        employ_nums = self._workbook.rows-1
        first_id_cell     = [ id_title_cell[ROW]+1,     id_title_cell[COL]     ]
        first_name_cell   = [ name_title_cell[ROW]+1,   name_title_cell[COL]   ]
        first_depart_cell = [ depart_title_cell[ROW]+1, depart_title_cell[COL] ]
        first_adjust_cell = [ adjust_title_cell[ROW]+1, adjust_title_cell[COL] ]
        for n in range(employ_nums):
            depart = self._workbook.get_cell_value(first_depart_cell[ROW] + n, first_depart_cell[COL])
            if not adjust_data.has_key(depart):
                adjust_data.update( {depart: {}} )
            employ_id = self._workbook.get_cell_value(first_id_cell[ROW] + n, first_id_cell[COL])
            employ_name = self._workbook.get_cell_value(first_name_cell[ROW] + n, first_name_cell[COL])
            data = self._workbook.get_cell_value(first_adjust_cell[ROW] + n, first_adjust_cell[COL])
            adjust_data[depart].update( { employ_id: {"name": employ_name, \
                                                      "vacday": self._adjust_data_to_vacation_day_dict(data)} } )
        return adjust_data
    
    def _check_adjust_data_format(self):
        data_fmt_ok = True
        employ_nums       = self._workbook.rows-1
        first_name_cell   = [ name_title_cell[ROW]+1,   name_title_cell[COL]   ]
        first_adjust_cell = [ adjust_title_cell[ROW]+1, adjust_title_cell[COL] ]
        for n in range(employ_nums):
            data = self._workbook.get_cell_value(first_adjust_cell[ROW] + n, first_adjust_cell[COL])
            if data is None:
                # 如果读取的是空Cell， 返回 False
                (rtr, res) = (False, "Empty Cell") 
            else:
                (rtr, res) = self._is_data_valid(data)
            if rtr is False:
                data_fmt_ok = False
                employ_name = self._workbook.get_cell_value(first_name_cell[ROW] + n, first_name_cell[COL])
                sys.stderr.write("(Line %d, Employ: %s) %s!\n"%(n+2, employ_name, res))
        return data_fmt_ok
    
    def _is_data_valid(self, data):
        valid_fmt = True
        invalid_fmt = False
        if not len(data): return (valid_fmt, "")
        
        data_list = data.split(';')
        if not len(data_list):
            return (invalid_fmt, "The data is invalid in cell")
        #print "data: ", [data]
        #print "data_list: ", [data_list]
        
        for vd in data_list:
            vac_and_days =  vd.split("(")
            if vac_and_days[0] == u'\n': 
                continue
            else:
                vacation_name = vac_and_days[0]
                if not len(vacation_name): continue
                #print [vac_and_days], len(vac_and_days), "len(vacation_name): ", len(vacation_name)
                if vacation_name[0] == u'\n': 
                    vacation_name = vacation_name[1:len(vacation_name)]
                # 数据库中没有该休假名
                if not vacation_name in VALID_VACATION_NAME:
                    return (invalid_fmt, "%s is not in vacation_name_db"%vacation_name)
                
            if not re.search(r'\)$', vac_and_days[1]):
                return (invalid_fmt, "The separator is invalid")
            else:
                days = vac_and_days[1][0:len(vac_and_days[1])-1]
            
            # 括号里没有数据
            if len(days) < 1:
                return (invalid_fmt, "Not data in the parenthesis")
            
            vac_days = days.split(", ")
            if len(vac_days) < 1: return invalid_fmt
            for d in vac_days:
                if re.search(r'\D', d): 
                    return (invalid_fmt, "%s is Invalid day"%d)
                d = int(d)
                if not (d >= 1 and d <= 31):
                    return (invalid_fmt, "%s is Invalid day"%d)
        
        return (valid_fmt, "")
        
    def _adjust_data_to_vacation_day_dict(self, raw_data): 
        vacation_dict = VACATION_STRUCT.copy()
        
        if not len(raw_data):
            return vacation_dict
        
        data_list = raw_data.split(';')
        for data in data_list:
            vac_and_days = data.split("(")
            
            if vac_and_days[0] == u'\n': 
                continue
            else:
                vacation_name = vac_and_days[0]
                
            if vacation_name[0] == u'\n': 
                vacation_name = vacation_name[1:len(vacation_name)]
                if vacation_name == u"上午" or \
                   vacation_name == u"下午" or \
                   vacation_name == u"工时不足":
                    continue
                
            days = vac_and_days[1][0:len(vac_and_days[1])-1]
            days_list = days.split(", ")
            
            if VACATION_NAME_TO_VAR.has_key(vacation_name):
                vacation_dict[VACATION_NAME_TO_VAR[vacation_name]] = len(days_list)
            else:
                vacation_dict[OTHER_LEAVE] = len(days_list)
        
        return vacation_dict
        
    def _write_table_header(self):
        self._workbook.write_cell_string(sn_title_cell[ROW],     sn_title_cell[COL],     sn_title_name)
        self._workbook.write_cell_string(id_title_cell[ROW],     id_title_cell[COL],     id_title_name)
        self._workbook.write_cell_string(name_title_cell[ROW],   name_title_cell[COL],   name_title_name)
        self._workbook.write_cell_string(absent_title_cell[ROW], absent_title_cell[COL], absent_title_name)   
        self._workbook.write_cell_string(depart_title_cell[ROW], depart_title_cell[COL], depart_title_name)
        self._workbook.write_cell_string(adjust_title_cell[ROW], adjust_title_cell[COL], adjust_title_name)
    
    def _open_excel(self, readonly=False):
        wb = OpenPyExcel.OpenPyExcel(attend_check_workbook_name)
        if wb.load_workbook(readonly) is False:
            sys.stderr.write("kaoqin Error: Loaded %s failure.\n"%self.workbook_name)
            self._workbook = None
            return False
        else:
            self._workbook = wb
            return True
            
    def _close_excel(self, save=False):
        if self._workbook.close(save):
            return True
        else:
            sys.stderr.write("kaoqin Error: Saved %s failure.\n"%self.workbook_name)
            return False
        
    def _load_summary_sheet(self):
        wb = AttendWorkbook.SummarySheet()
        if not wb.is_open:
            sys.stderr.write( "kaoqin Error: Loaded %s failure from %s.\n"%(u'考勤汇总 Sheet', u'标准报表.xls') )
            self._summary_wb = None
            return False
        self._summary_wb = wb
        return True

    def _load_record_sheet(self):
        wb = AttendWorkbook.RecordSheet()
        if not wb.is_open:
            sys.stderr.write( "kaoqin Error: Loaded %s failure from %s.\n"%(u'考勤记录 Sheet', u'标准报表.xls') )
            self._record_wb = None
            return False
        self._record_wb = wb
        return True
    
    def _add_sheet(self):
        if self._workbook.add_sheet(self.sheet_name, 'w') is False:
            sys.stderr.write("kaoqin Error: Added %s sheet failure.\n"%self.sheet_name)
            return False
        return True
            
    def _open_sheet(self):
        if self._workbook.open_sheet(self.sheet_name) is False:
            sys.stderr.write("kaoqin Error: Opened %s sheet failure.\n"%self.sheet_name)
            return False
        return True
    
    def _write_check_data(self):             
        reg_absent_day = re.compile(r"(\,\s+)$")
        row = start_write_info_row
        for n in self._summary_wb.employee_base_info:
            #缺勤明细处理
            absent_info = ""
            kaoqin_dict = KAOQIN_STRUCT.copy()
            
            # 写入工号、员工姓名的起始列
            col = start_write_info_col
            #写入序号
            self._workbook.write_cell_number(row, col, n)
            _id = self._summary_wb.employee_base_info[n]["id"]
            #写入工号
            self._workbook.write_cell_number(row, col+1, _id)
            #写入员工姓名
            self._workbook.write_cell_string(row, col+2, self._summary_wb.employee_base_info[n]["name"])
            #写入员工所在的部门
            self._workbook.write_cell_string(row, col+3, self._summary_wb.employee_base_info[n]["department"])
            
            for day in range(self._record_wb.attend_days):
                # range是以 0 开始为索引的
                day += 1
                absent = self._record_wb.attend_record_info[_id][day]
                if  absent == NORMAL_ATTEND or \
                    absent == NORMAL_DAYOFF or \
                    absent == ANNUAL_LEAVE:
                        continue
                else:
                    kaoqin_dict[absent] += "%s, "%day
    
            for absent in kaoqin_dict:
                if kaoqin_dict[absent] == "": continue
                #if not absent_info == "": absent_info += "\r\n"
                absent_days = re.sub(reg_absent_day, '', kaoqin_dict[absent])
                absent_info += "%s(%s);\r\n"%(KAOQIN_DESCRIBE[absent], absent_days)
    
            self._workbook.write_cell_string(row, start_write_absent_col, absent_info)   
            row += 1 
            
class vacation():
    def __init__(self):
        pass
    
        
class fanbu():
    def __init__(self, year, month, adjust_data):
        self.year = year
        self.month = month
        self.workbook_name = MEAL_ALLOWANCE_WORKBOOK_NAME
        self.sheet_name = "%s-%s"%(self.year,self.month)
        self._workbook = None
        self._worksheet = None
        self._adjust_dict = adjust_data
        self.workdays = int(Profile.Profile().workdays)
        
        self.vacation_cell_dict = {EVECTION:         EVECTION_COL,       \
                                   ANNUAL_LEAVE:     ANNUAL_LEAVE_COL,   \
                                   SICK_LEAVE:       SICK_LEAVE_COL,     \
                                   MATERNITY_LEAVE:  MATERNITY_LEAVE_COL,\
                                   CASUAL_LEAVE:     CASUAL_LEAVE_COL,   \
                                   MARRIAGE_LEAVE:   MARRIAGE_LEAVE_COL, \
                                   FUNERAL_LEAVE:    FUNERAL_LEAVE_COL,  \
                                   OTHER_LEAVE:      OTHER_LEAVE_COL     \
                                   }

    def Create(self):
        self._open_workbook()
        if self._workbook is None:
            return 
        
        if self._add_sheet():
            if not self._open_sheet():
                return
        else:
            return
        
        self._write_title()
        self._write_vacation_data()
        self._close_workbook(save=True)
        
    def _write_title(self):
        meal_allownance_title = (u"上海分公司 %s年%s月份考勤记录表")%(self.year, self.month)
        self._workbook.write_cell_by_coordinate(MEAL_ALLOWANCE_TITILE_CELL, meal_allownance_title)
        self._workbook.write_cell_by_coordinate(MEAL_ALLOWANCE_AUTHOR_TITILE_CELL, MEAL_ALLOWANCE_AUTHOR_TITILE)
        self._workbook.write_cell_by_coordinate(MEAL_ALLOWANCE_AUTHOR_CELL, MEAL_ALLOWANCE_AUTHOR)
        
    def _write_table_header(self, row):
        header_num = len(TABLE_HEADER_COL_LIST_FANBU)
        num = 0
        while( num < (header_num - 1) ):
            #cell_loc = TABLE_HEADER_COL_LIST_FANBU[num]
            col = TABLE_HEADER_COL_LIST_FANBU[num]
            header_name = TABLE_HEADER_COL_LIST_FANBU[num + 1]
            self._workbook.write_cell_string(row, col, header_name)
            num += 2
            
    def _write_vacation_data(self):
        row = FIRST_RECORD_ROW
            
        for depart in self._adjust_dict:
            self._write_table_header(row)
            row += 1
            sn = 1
            for employ_id in self._adjust_dict[depart]:
                #写入 序号
                self._workbook.write_cell_string(row, SN_COL, sn)
                #写入 工号
                self._workbook.write_cell_string(row, ID_COL, self.employ_id_competion(employ_id))
                #写入 姓名
                self._workbook.write_cell_string(row, NAME_COL, self._adjust_dict[depart][employ_id]["name"])
                #写入 本月出勤天数
                self._workbook.write_cell_string(row, WORKDAY_COL, self.workdays)
                
                attend_days = self.workdays
                vacation_dict = self._adjust_dict[depart][employ_id]["vacday"]
                for vac_name in vacation_dict:
                    if vacation_dict[vac_name] == 0:
                        continue
                    else:
                        #print "vacation_dict[vac_name]: ", vacation_dict[vac_name]
                        attend_days -= int(vacation_dict[vac_name])
                        #写入 相应假期的天数
                        self._workbook.write_cell_string(row, self.vacation_cell_dict[vac_name], \
                                                        vacation_dict[vac_name])
                        
                #写入 实际出勤天数
                self._workbook.write_cell_string(row, ATTEND_DAY_COL, attend_days)
                #写入 饭贴
                self._workbook.write_cell_string(row, MEAL_ALLOWANCE_COL, attend_days * MEAL_ALLOWANCE_AMOUNT)
                sn += 1
                row += 1
                
    def employ_id_competion(self, raw_id):
        id_len = 6
        raw_id = str(raw_id)
        raw_id_len = len(raw_id)
        if raw_id_len < id_len:
            while( len(raw_id) < id_len ):
                raw_id = "0%s"%raw_id
        return raw_id
                
    def _open_workbook(self):
        self._workbook = OpenPyExcel.OpenPyExcel(self.workbook_name)
        if self._workbook.load_workbook() is False:
            Common.pause(u"打开 %s 失败\n"%self.workbook_name)
            self._workbook = None
            
    def _close_workbook(self, save=True):
        if self._workbook.close(save):
            if save is True:
                result = u"\"%s\" %s\n"%(self.workbook_name, u"已生成。") 
            else:
                result = " "
        else:
            result = u"\"%s\" %s\n"%(self.workbook_name, u"生成失败。")
        return result   
    
    def _add_sheet(self):
        if self._workbook:
            if self._workbook.add_sheet(self.sheet_name, 'w'):
                return True
            else:
                return False
    
    def _open_sheet(self):
        if self._workbook:
            if self._workbook.open_sheet(self.sheet_name):
                return True
            else:
                return False




