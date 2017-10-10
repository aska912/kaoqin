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
            NORMAL_ATTEND:        u'��������',     \
            NORMAL_DAYOFF:        u'˫����',      \
            ANNUAL_LEAVE:         u'���',       \
            NO_ATTEND_RECORD:     u'ȫ��',       \
            NO_MORNING_REC:       u'����',       \
            NO_AFTERNON_REC:      u'����',       \
            ABSENT_MORNING:       u'����',       \
            ABSENT_AFTERNON:      u'����',       \
            ONE_ATTEND_RECORD:    u'���ο���ʱ��',  \
            NO_ENOUGH_WORK_TIME:  u'��ʱ����',     \
            UNKONW_ATTEND_STATE:  u'δ֪״̬'}





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

VACATION_DESCRIBE = { EVECTION:        u'����', \
                      ANNUAL_LEAVE:    u'���', \
                      SICK_LEAVE:      u'����', \
                      MATERNITY_LEAVE: u'����', \
                      CASUAL_LEAVE:    u'�¼�', \
                      MARRIAGE_LEAVE:  u'���', \
                      FUNERAL_LEAVE:   u'ɥ��', \
                      OTHER_LEAVE:     u'����'  }

VACATION_NAME_TO_VAR = { u'����': EVECTION,        \
                         u'���': ANNUAL_LEAVE,    \
                         u'����': SICK_LEAVE,      \
                         u'����': MATERNITY_LEAVE, \
                         u'�¼�': CASUAL_LEAVE,    \
                         u'ȫ��': CASUAL_LEAVE,    \
                         u'���': MARRIAGE_LEAVE,  \
                         u'ɥ��': FUNERAL_LEAVE,   \
                         u'����': OTHER_LEAVE }

VALID_VACATION_NAME = [  u'����', u'���', u'����', u'����', \
                         u'�¼�', u'ȫ��', u'���', u'ɥ��', \
                         u'����', u'����', u'����', u'����', \
                         u'��ʱ����' ]

TABLE_HEADER_COL_LIST_FANBU = [                   
                          1,  u"���",         \
                          2,  u"����",         \
                          3,  u"����",         \
                          4,  u"���³�������",  \
                          5,  u"��������",      \
                          6,  u"�������",      \
                          7,  u"��������",      \
                          8,  u"��������",      \
                          9,  u"�¼�����",      \
                          10, u"�������",      \
                          11, u"ɥ������",      \
                          12, u"����",          \
                          13, u"ʵ�ʳ�������",   \
                          14, u"����",          \
                          15, u"˵��",          \
                          16, u"ǩ��ȷ��"       \
                        ]



