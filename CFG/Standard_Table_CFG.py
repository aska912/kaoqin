# -*- coding: cp936 -*-

from Global import ROW
from Global import COL


adj = 1

###########################################################
#  ��׼�������ɿ��ڻ����ɵ�workbook
#  ��׼�����������4��Sheet��
#      �쳣ͳ�� -- abnormal_sheet
#      ���ڼ�¼ -- record_sheet
#      ���ڻ��� -- summary_sheet
#      �Ű���Ϣ -- arrange_sheet
#       
# 
attend_workbook_name    = u'��׼����.xls'
abnormal_sheet_name     = u'�쳣ͳ��'
record_sheet_name       = u'���ڼ�¼'
summary_sheet_name      = u'���ڻ���'
arrange_sheet_name      = u'�Ű���Ϣ'

#---------------���ڻ���-----------------------
#�����ǿ��ڻ���Sheet����������������
#��Ч������ʼ��
start_row_summary_sheet = 2 - adj
#��Ч������ʼ��
start_col_summary_sheet = 1 - adj

#ͳ����������
date_row_summary_sheet = 2 - adj
date_col_summary_sheet = 2 - adj

#Ա����Ϣ��ʼ��
start_empolyee_row_summary_sheet        = 5 - adj
#������
id_col_summary_sheet                    = 1 - adj
#������                                                                  
name_col_summary_sheet                  = 2 - adj
#����������                                                              
department_col_summary_sheet            = 3 - adj
#��׼����ʱ����                                                          
stand_attend_hours_col_summary_sheet    = 4 - adj
#��׼����������                                                          
stand_attend_days_col_summary_sheet     = 12 - adj
#������                                                                  
absent_col_summary_sheet                = 14 - adj


#---------------���ڼ�¼-----------------------
#�����ǿ��ڼ�¼Sheet����������������
#��Ч������ʼ��
start_row_record_sheet = 3 - adj
#��Ч������ʼ��
start_col_record_sheet = 1 - adj

#ͳ����������
date_row_record_sheet = 3 - adj
date_col_record_sheet = 3 - adj

#Ա����Ϣ��ʼ��
start_empolyee_row_record_sheet         = 5 - adj
#Ա�����ڼ�¼��ʼ��
start_attend_row_record_sheet           = 6 - adj

#������
id_col_record_sheet                     = 3 - adj

#ͳ��������ʼ��
first_day_col_recold_sheet              = 1 - adj

start_work_time = "9:05"
nooning_time    = "11:30"
afternon_time   = "13:00"
close_work_time = "16:25"
normal_work_hours = float(7.0)
half_work_hours = float(4.0)



###############################################################################


#################################### ���ں˶Ա����� ############################
#
#
#
#
#
attend_check_workbook_name = u'���ں˶Ա�.xlsx'

sn_title_cell       = [1-adj, 1-adj]
sn_title_name       = u'���'
id_title_cell       = [1-adj, 2-adj]
id_title_name       = u'����'
name_title_cell     = [1-adj, 3-adj]
name_title_name     = u'����'
absent_title_cell   = [1-adj, 4-adj]
absent_title_name   = u'ȱ����ϸ'

# ��ʼд��Ա����Ϣ������
start_write_info_row = sn_title_cell[ROW] + 1
start_write_info_col = sn_title_cell[COL]

start_write_absent_row = start_write_info_row
start_write_absent_col = absent_title_cell[COL]










