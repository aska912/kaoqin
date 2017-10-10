# -*- coding: cp936 -*-
#!/usr/bin/env python

import sys, os.path
import Common
import Profile, kaoqin


def main_option_menu():
    sys.stdout.write(u"(0) 查看/修改配置文件\n")
    sys.stdout.write(u"(1) 生成考勤核对表\n")
    sys.stdout.write(u"(2）生成饭补\n")
    sys.stdout.write(u"(3) 退出\n")

def profile_option_menu():
    sys.stdout.write(u"(p) 查看配置文件\n")
    sys.stdout.write(u"(m) 修改配置文件\n")
    sys.stdout.write(u"(r) 返回\n")
    
def main():
    main_option_menu()
    while True:
        opt = raw_input( "%s"%Common.unicode_to_str(u"请输入选项： ") )
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
            sys.stderr.write(u"错误选项，请重新输入\n\n")
            continue


if __name__ == "__main__":  
    main()
