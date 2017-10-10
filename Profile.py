# -*- coding: cp936 -*-

import sys, os.path, Common


class Profile():
    def __init__(self):
        self.filename = "profile"
        self._fn = None
        
        if not self.isexist: self.create()
        
    @property
    def isexist(self):
        """
        if exist, then return True
        """
        return os.path.isfile(self.filename)
    
    @property
    def workdays(self):
        #default_value = 21
        lines = self.readlines()
        if len(lines):
            for ln in lines:
                var_name = ln.split(":")[0]
                if var_name == "working days":
                    return ln.split(":")[1]
        #return default_value  

    @workdays.setter
    def workdays(self, days):
        self._set_workdays(days)
            
    def _set_workdays(self, days):
        if days < 15 and days > 23: days = 21
        find = False
        lines = self.readlines()
        if self.open():
            if len(lines):
                for ln in lines:
                    var_name = ln.split(":")[0]
                    if var_name == "working days":
                        self.writeline("%s:%s\n"%(var_name, days))
                        find = True
                    else:
                        self.writeline("%s"%ln)
            if find is False:
                self.writeline("working days:%s\n"%days)
            self.close()
    
    @property
    def holidays(self):
        """
        return int list
        """
        default_value = []
        days_list = default_value
        lines = self.readlines()
        if len(lines):
            for ln in lines:
                var_name = ln.split(":")[0]
                if var_name == "holidays":
                    days =  ln.split(":")[1]
                    if days == "\n": return default_value
                    for d in days.split(","):
                        days_list.append(int(d))
                    return days_list
        return default_value 

    @holidays.setter
    def holidays(self, days):
        self._set_holidays(days)
        
    def _set_holidays(self, days):
        find = False
        lines = self.readlines()
        if self.open():
            if len(lines):
                for ln in lines:
                    var_name = ln.split(":")[0]
                    if var_name == "holidays":
                        self.writeline("%s:%s\n"%(var_name, days))
                        find = True
                    else:
                        self.writeline("%s"%ln)
            if find is False:
                self.writeline("holidays:%s\n"%days)
            self.close()  
    
    def dump(self):
        if self.open(onlyread=True):
            p = self._fn.readlines()
            self.close()
            for ln in p: sys.stdout.write(ln)
            sys.stdout.write("\n")
            
    def modify(self):
        sys.stdout.write(u"本月有效工作天数(默认: 21): ")
        workdays = raw_input()
        sys.stdout.write(u"法定假日休息日(格式： 1,2,3 | 默认为空): ")
        holidays = raw_input()
        self._set_workdays(workdays)
        self._set_holidays(holidays)
        
    def create(self):
        if self.open():
            self.close()
            return True
        else:
            return False
    
    def open(self, onlyread=False):
        if onlyread: 
            mode = "r"
        else:
            mode = "w"
        try:
            self._fn = open(self.filename, mode)
            return True
        except:
            sys.stderr.write(u"没有找到指定的profile\n")
            self._fn = None
            return False
        
    def writeline(self, oneline):
        if self._fn is not None:
            self._fn.write(oneline)
    
    def readlines(self):
        if self.open(onlyread=True):
            lines = self._fn.readlines()
            self.close()
            return lines
        else:
            return []
        
    def close(self):
        self._fn.close()


def profile_main():
    while True:
        opt = raw_input( "%s"%Common.unicode_to_str(u"[profile]请输入选项： ") )
        if opt == 'p':
            Profile().dump()
        elif opt == 'm':
            Profile().modify()
        elif opt == 'r':
            return
        else:
            sys.stderr.write(u"错误选项，请重新输入\n\n")
            continue
        
