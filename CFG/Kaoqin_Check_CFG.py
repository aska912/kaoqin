# -*- coding: cp936 -*-

# ֻ������ openpyxl
# openpyxl��row/column�Ǵ�1��ʼ�����

from Global import ROW
from Global import COL


#################################### ���ں˶Ա����� ############################

attend_check_workbook_name = u'���ں˶Ա�.xlsx'

sn_title_cell       = [1, 1]
sn_title_name       = u'���'
id_title_cell       = [1, 2]
id_title_name       = u'����'
name_title_cell     = [1, 3]
name_title_name     = u'����'
depart_title_cell   = [1, 4]
depart_title_name   = u'����'
absent_title_cell   = [1, 5]
absent_title_name   = u'ȱ����ϸ'

# ��ʼд��Ա����Ϣ������
start_write_info_row = sn_title_cell[ROW] + 1
start_write_info_col = sn_title_cell[COL]

start_write_absent_row = start_write_info_row
start_write_absent_col = absent_title_cell[COL]



#################################### ���ڵ��������� ############################
adjust_title_cell   = [1, 6]
adjust_title_name   = u'����'












