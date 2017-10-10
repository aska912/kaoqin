# -*- coding: cp936 -*-

import sys
import xlrd, MyObj


class XlrdExcel(MyObj.MyObj):
    """
    Only for read excel
    """
    def __init__(self, filename, **args):
        super(XlrdExcel, self).__init__()
        self.filename = filename
        self._workbook = None
        self._sheet = None
    
    def load_workbook(self):
        try:
            self._workbook = xlrd.open_workbook(self.filename)
            return True
        except:
            sys.stderr.write( "XlrdExcel Error: \"%s\" No such file.\n"%(self.filename) )
            self._workbook = None
            return False
            
    def open_sheet(self, sheet_name="Sheet1"):
        if self._workbook is None: 
            self._sheet = None
        else:
            self._sheet = self._workbook.sheet_by_name(sheet_name)
        
    def get_cell_value(self, row, col):
        if self._sheet is None: return None
        return self._sheet.cell_value(row, col)

    @property
    def rows(self):
        if self._sheet is None: return 0
        return self._sheet.nrows

    @property
    def columns(self):
        if self._sheet is None: return 0
        return self._sheet.ncols

    def get_sheet_list(self):
        if self._sheet is None: return []
        return self._workbook.sheet_names()

