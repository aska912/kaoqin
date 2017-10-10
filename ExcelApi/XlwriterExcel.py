# -*- coding: cp936 -*-

import sys
import xlsxwriter, MyObj



class XlwriterExcel(MyObj.MyObj):
    """
    Only for write excel
    """
    def __init__(self, filename, **args):
        super(XlwriterExcel, self).__init__()
        self.filename = filename
        self._workbook = None
        self._sheet = None
    
    def create_workbook(self):
        try:
            self._workbook = xlsxwriter.Workbook(self.filename)
            return True
        except:
            #sys.stderr.write(u"创建 "+self.filename+u" 失败"+"\n")
            self._workbook = None
            return False
            
    def add_sheet(self, sheet_name=None):
        if self._workbook is None: self._sheet = None
        self._sheet = self._workbook.add_worksheet(sheet_name)
            
    def write_cell(self, row, col, data):
        if self._sheet is None: return
        self._sheet.write_column(row, col, data)
        
    def write_cell_string(self, row, col, str_data=""):
        if self._sheet is None: return
        self._sheet.write_string(row, col, str_data)
        
    def write_cell_number(self, row, col, num=0):
        if self._sheet is None: return
        self._sheet.write_number(row, col, num)
        
        
    def save_workbook(self):
        try:
            self._workbook.close()
            return True
        except IOError:
            sys.stderr.write(u"错误： 创建  \""+self.filename+u"\" 失败。该文件可能已被打开！"+"\n")
            return False
        
        
        
        