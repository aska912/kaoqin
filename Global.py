# -*- coding: cp936 -*-

ROW = 0
COL = 1

UNKONW_ATTEND_STATE = 100
NORMAL_ATTEND       = 200
NORMAL_DAYOFF       = 300
ANNUAL_LEAVE        = 400
NO_ATTEND_RECORD    = 500
ABSENT_MORNING      = 600
ABSENT_AFTERNON     = 700
ONE_ATTEND_RECORD   = 800
NO_ENOUGH_WORK_TIME = 900
NO_MORNING_REC      = 1000
NO_AFTERNON_REC     = 1100

KAOQIN_STRUCT= {                           \
            NORMAL_ATTEND:          "",    \
            NORMAL_DAYOFF:          "",    \
            ANNUAL_LEAVE:           "",    \
            NO_ATTEND_RECORD:       "",    \
            NO_MORNING_REC:         "",    \
            NO_AFTERNON_REC:        "",    \
            ABSENT_MORNING:         "",    \
            ABSENT_AFTERNON:        "",    \
            ONE_ATTEND_RECORD:      "",    \
            NO_ENOUGH_WORK_TIME:    "",    \
            UNKONW_ATTEND_STATE:    ""}

KAOQIN_DESCRIBE= {\
            NORMAL_ATTEND:        u'正常考勤',     \
            NORMAL_DAYOFF:        u'双休日',      \
            ANNUAL_LEAVE:         u'年假',       \
            NO_ATTEND_RECORD:     u'全天',       \
            NO_MORNING_REC:       u'上午',       \
            NO_AFTERNON_REC:      u'下午',       \
            ABSENT_MORNING:       u'上午',       \
            ABSENT_AFTERNON:      u'下午',       \
            ONE_ATTEND_RECORD:    u'单次考勤时间',  \
            NO_ENOUGH_WORK_TIME:  u'工时不足',     \
            UNKONW_ATTEND_STATE:  u'未知状态'}





ANNUAL_LEAVE    = 1200
SICK_LEAVE      = 1300
MATERNITY_LEAVE = 1400
CASUAL_LEAVE    = 1500
MARRIAGE_LEAVE  = 1600
FUNERAL_LEAVE   = 1700
OTHER_LEAVE     = 1800
EVECTION        = 1900
HALF_LEAVE      = 2000

VACATION_STRUCT = { ANNUAL_LEAVE:    0, \
                    SICK_LEAVE:      0, \
                    MATERNITY_LEAVE: 0, \
                    CASUAL_LEAVE:    0, \
                    MARRIAGE_LEAVE:  0, \
                    FUNERAL_LEAVE:   0, \
                    HALF_LEAVE:      0, \
                    OTHER_LEAVE:     0}

VACATION_DESCRIBE = { EVECTION:        u'出差', \
                      ANNUAL_LEAVE:    u'年假', \
                      SICK_LEAVE:      u'病假', \
                      MATERNITY_LEAVE: u'产假', \
                      CASUAL_LEAVE:    u'事假', \
                      MARRIAGE_LEAVE:  u'婚假', \
                      FUNERAL_LEAVE:   u'丧假', \
                      OTHER_LEAVE:     u'其他'  }

VACATION_NAME_TO_VAR = { u'出差': EVECTION,        \
                         u'年假': ANNUAL_LEAVE,    \
                         u'病假': SICK_LEAVE,      \
                         u'产假': MATERNITY_LEAVE, \
                         u'事假': CASUAL_LEAVE,    \
                         u'全天': CASUAL_LEAVE,    \
                         u'婚假': MARRIAGE_LEAVE,  \
                         u'丧假': FUNERAL_LEAVE,   \
                         u'其他': OTHER_LEAVE }

VALID_VACATION_NAME = [  u'出差', u'年假', u'病假', u'产假', \
                         u'事假', u'全天', u'婚假', u'丧假', \
                         u'上午', u'下午', u'其他', u'半天', \
                         u'工时不足' ]

TABLE_HEADER_COL_LIST_FANBU = [                   
                          1,  u"序号",         \
                          2,  u"工号",         \
                          3,  u"姓名",         \
                          4,  u"本月出勤天数",  \
                          5,  u"出差天数",      \
                          6,  u"年假天数",      \
                          7,  u"病假天数",      \
                          8,  u"产假天数",      \
                          9,  u"事假天数",      \
                          10, u"婚假天数",      \
                          11, u"丧假天数",      \
                          12, u"其他",          \
                          13, u"实际出勤天数",   \
                          14, u"饭贴",          \
                          15, u"说明",          \
                          16, u"签名确认"       \
                        ]



