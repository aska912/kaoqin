# -*- coding: cp936 -*-

import datetime, time, re, sys


CN_ENCODE="gb2312"

ENCODE=CN_ENCODE

def value_type(var):
    tp = re.search(r"\'(\w+)\'",str(type(var)))
    if tp:
        return str( tp.group(1))
    else:
        return "unknown"

def file_is_exist(filename):
    try:
        pass
    except:
        pass
    
def unicode_to_int(var):
    if value_type(var) == "unicode":
        return int(var.encode(ENCODE))
    
def unicode_to_str(var):
    if value_type(var) == "unicode":
        return str(var.encode(ENCODE))

def get_current_year():
    return datetime.date.today().year

def get_current_month():
    return datetime.date.today().month    

def get_current_day():
    return datetime.date.today().day

def get_current_date(sprtr="-"):
    """
    default separtor is "-"
    return yy-mm-dd
    """
    return datetime.date.today().strftime("%Y-%m-%d")

def current_second():
    return datetime.time.time()

def date_to_timestamp(_date):
    return time.mktime(time.strptime(_date, "%Y-%m-%d"))

def timestamp_to_date(ts):
    return time.strftime("%Y-%m-%d", time.localtime(ts))

def datetime_to_timestamp(_date, _time):
    return time.mktime(time.strptime( "%s %s"%(_date, _time),  "%Y-%m-%d %H:%M") )

def get_year_from_timestamp(ts):
    return time.localtime(ts).tm_year

def get_month_from_timestamp(ts):
    return time.localtime(ts).tm_mon

def get_day_from_timestamp(ts):
    return time.localtime(ts).tm_mday

def get_weekday_name_from_timestamp(ts):
    return time.strftime("%a",time.localtime(ts))

def is_working_day(timestamp):
    wk_name = get_weekday_name_from_timestamp(timestamp)
    if wk_name == "Sun" or wk_name == "Sat":
        return False
    else:
        return True
    
def get_month_day(month, day):
    return "%s/%s"%(month, day) 

def pause(prmpt_str=None):
    if prmpt_str is not None:
        sys.stdout.write( "%s"%unicode_to_str(prmpt_str) )
    sys.stdout.write( "%s\n"%(u"请按任意键继续...") )
    return raw_input()
    

