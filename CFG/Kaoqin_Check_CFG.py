# -*- coding: cp936 -*-

# 只能用于 openpyxl
# openpyxl的row/column是从1开始计算的

from Global import ROW
from Global import COL


#################################### 考勤核对表配置 ############################

attend_check_workbook_name = u'考勤核对表.xlsx'

sn_title_cell       = [1, 1]
sn_title_name       = u'序号'
id_title_cell       = [1, 2]
id_title_name       = u'工号'
name_title_cell     = [1, 3]
name_title_name     = u'姓名'
depart_title_cell   = [1, 4]
depart_title_name   = u'部门'
absent_title_cell   = [1, 5]
absent_title_name   = u'缺勤明细'

# 开始写入员工信息的行列
start_write_info_row = sn_title_cell[ROW] + 1
start_write_info_col = sn_title_cell[COL]

start_write_absent_row = start_write_info_row
start_write_absent_col = absent_title_cell[COL]



#################################### 考勤调整表配置 ############################
adjust_title_cell   = [1, 6]
adjust_title_name   = u'调整'












