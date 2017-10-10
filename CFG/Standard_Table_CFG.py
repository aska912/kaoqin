# -*- coding: cp936 -*-

from Global import ROW
from Global import COL


adj = 1

###########################################################
#  标准报表是由考勤机生成的workbook
#  标准报表里面包含4个Sheet：
#      异常统计 -- abnormal_sheet
#      考勤记录 -- record_sheet
#      考勤汇总 -- summary_sheet
#      排班信息 -- arrange_sheet
#       
# 
attend_workbook_name    = u'标准报表.xls'
abnormal_sheet_name     = u'异常统计'
record_sheet_name       = u'考勤记录'
summary_sheet_name      = u'考勤汇总'
arrange_sheet_name      = u'排班信息'

#---------------考勤汇总-----------------------
#以下是考勤汇总Sheet里各个常用项的行列
#有效数据起始行
start_row_summary_sheet = 2 - adj
#有效数据起始列
start_col_summary_sheet = 1 - adj

#统计日期行列
date_row_summary_sheet = 2 - adj
date_col_summary_sheet = 2 - adj

#员工信息起始行
start_empolyee_row_summary_sheet        = 5 - adj
#工号列
id_col_summary_sheet                    = 1 - adj
#姓名列                                                                  
name_col_summary_sheet                  = 2 - adj
#所属部门列                                                              
department_col_summary_sheet            = 3 - adj
#标准工作时数列                                                          
stand_attend_hours_col_summary_sheet    = 4 - adj
#标准出勤天数列                                                          
stand_attend_days_col_summary_sheet     = 12 - adj
#旷工列                                                                  
absent_col_summary_sheet                = 14 - adj


#---------------考勤记录-----------------------
#以下是考勤记录Sheet里各个常用项的行列
#有效数据起始行
start_row_record_sheet = 3 - adj
#有效数据起始列
start_col_record_sheet = 1 - adj

#统计日期行列
date_row_record_sheet = 3 - adj
date_col_record_sheet = 3 - adj

#员工信息起始行
start_empolyee_row_record_sheet         = 5 - adj
#员工考勤记录起始行
start_attend_row_record_sheet           = 6 - adj

#工号列
id_col_record_sheet                     = 3 - adj

#统计日期起始列
first_day_col_recold_sheet              = 1 - adj

start_work_time = "9:05"
nooning_time    = "11:30"
afternon_time   = "13:00"
close_work_time = "16:25"
normal_work_hours = float(7.0)
half_work_hours = float(4.0)



###############################################################################


#################################### 考勤核对表配置 ############################
#
#
#
#
#
attend_check_workbook_name = u'考勤核对表.xlsx'

sn_title_cell       = [1-adj, 1-adj]
sn_title_name       = u'序号'
id_title_cell       = [1-adj, 2-adj]
id_title_name       = u'工号'
name_title_cell     = [1-adj, 3-adj]
name_title_name     = u'姓名'
absent_title_cell   = [1-adj, 4-adj]
absent_title_name   = u'缺勤明细'

# 开始写入员工信息的行列
start_write_info_row = sn_title_cell[ROW] + 1
start_write_info_col = sn_title_cell[COL]

start_write_absent_row = start_write_info_row
start_write_absent_col = absent_title_cell[COL]










