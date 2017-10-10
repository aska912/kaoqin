# -*- coding: cp936 -*-

import Common, Profile
from Global import *
from CFG.Standard_Table_CFG import *

class AttendTimeProcess(object):
    def __init__(self, attend_date=""):
        if attend_date == "":
            self.date   = attend_date
        else:
            self.date = Common.get_current_date()
            
        self.start_work_sec  = Common.datetime_to_timestamp(self.date, start_work_time)
        self.nooning_sec     = Common.datetime_to_timestamp(self.date, nooning_time)
        self.afternoon_sec   = Common.datetime_to_timestamp(self.date, afternon_time)
        self.close_work_sec  = Common.datetime_to_timestamp(self.date, close_work_time)
        
        
    def get_attend_state(self, arrive_time, leave_time=""):
        arrive_ts = Common.datetime_to_timestamp(self.date, arrive_time)
        if leave_time == "":
            return self.one_attend_time(arrive_ts)
        else:
            leave_ts = Common.datetime_to_timestamp(self.date, leave_time)
            
        if self.is_normal_attend(arrive_ts, leave_ts):
            return NORMAL_ATTEND
        
        elif self.is_morning_absent(arrive_ts, leave_ts):
            return NO_MORNING_REC
        
        elif self.is_afternon_absent(arrive_ts, leave_ts):
            return NO_AFTERNON_REC
        
        elif self.is_noenough_workhour(arrive_ts, leave_ts):
            return NO_ENOUGH_WORK_TIME
        
        else:
            return UNKONW_ATTEND_STATE
        
    
    def one_attend_time(self, attend_ts):
        if attend_ts > self.nooning_sec:
            # ȱ����򿨼�¼
            return NO_MORNING_REC
        else:
            return NO_AFTERNON_REC

    
    def is_normal_attend(self, arrive_ts, leave_ts):
        workhours = self.get_work_hours( arrive_ts, leave_ts)
        if (arrive_ts <= self.start_work_sec and leave_ts >= self.close_work_sec):
            # �����ϰ�ʱ�䵽��������ʱ���°�
            return True
        elif (arrive_ts <= self.start_work_sec and workhours > normal_work_hours):
            # �����ϰ�ʱ�䵽���ҹ�ʱ����7h
            return True 
        elif (arrive_ts >= self.start_work_sec and arrive_ts <= self.nooning_sec) and \
             (workhours > normal_work_hours):
            # ���������ϰ�ʱ�䣬����������ʱ�䵽�ġ��ҹ�ʱ����7h
            return True
        else:
            return False
    
    
    def is_morning_absent(self, arrive_ts, leave_ts):
        if (arrive_ts > self.nooning_sec):
            return True
        else:
            return False
    
    
    def is_afternon_absent(self, arrive_ts, leave_ts):
        workhours = self.get_work_hours( arrive_ts, leave_ts)
        if (arrive_ts < self.nooning_sec and workhours <= half_work_hours):
            return True
        else:
            return False
        
    
    def is_noenough_workhour(self, arrive_ts, leave_ts):
        workhours = self.get_work_hours( arrive_ts, leave_ts)
        if workhours > half_work_hours and workhours < normal_work_hours:
            return True
        else:
            return False
        
    
    def get_work_hours(self, arrive_ts, leave_ts):
        return float((leave_ts-arrive_ts)/3600)
    
    
    
    
    
    
    
    
    
    
