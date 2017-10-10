# -*- coding: cp936 -*-
#!/usr/bin/env python

import sys, os.path
import Common
import Profile, kaoqin


def main_option_menu():
    sys.stdout.write(u"(0) �鿴/�޸������ļ�\n")
    sys.stdout.write(u"(1) ���ɿ��ں˶Ա�\n")
    sys.stdout.write(u"(2�����ɷ���\n")
    sys.stdout.write(u"(3) �˳�\n")

def profile_option_menu():
    sys.stdout.write(u"(p) �鿴�����ļ�\n")
    sys.stdout.write(u"(m) �޸������ļ�\n")
    sys.stdout.write(u"(r) ����\n")
    
def main():
    main_option_menu()
    while True:
        opt = raw_input( "%s"%Common.unicode_to_str(u"������ѡ� ") )
        if opt == '1':
            #kaoqin.kaoqin_check_main()
            kaoqin.kaoqin().Create()
            continue
        elif opt == '2':
            #kaoqin.kaoqin_adjust_main()
            kaoqin.kaoqin().Fanbu()
            continue
        elif opt == '3':
            sys.exit(0)
        elif opt == '0':
            profile_option_menu()
            Profile.profile_main()
            main_option_menu()
        else:
            sys.stderr.write(u"����ѡ�����������\n\n")
            continue


if __name__ == "__main__":  
    main()
