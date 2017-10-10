# -*- codeing: cp936 -*-

import win32com.client
from ExcelApi import MyObj



class WinExcel(MyObj):
    
    def __init__(self, filename, **args):
        self.filename = filename
        self._excel = None
        self._workbook = None
        self._active_sheet = None
        
        if not self.__init_excel_app():
            return
    
    def load_workbook(self):
        if self._excel is None:
            return
    
    def open_sheet(self):
        pass
    
    def add_sheet(self):
        pass
    
    def __init_excel_app(self, visable=False):
        try:
            self._excel = win32com.client.DispatchEx('Excel.Application')
            self._excel.Visable = visable
            return True
        except:
            self._excel = None
            return False
        
        
        
class Excel():
    def __init__(self, **args):
        pass
    
    @property
    def visable(self):
        pass
    
    @visable.setter
    def visable(self, open=False):
        pass
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    