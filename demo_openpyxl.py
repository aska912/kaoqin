# -*- coding: cp936 -*-
#!/usr/bin/env python

import sys, os
import _ExcelApi

if __name__ == "__main__":
    excel_filename = "test.xlsx"
    if os.path.isfile(excel_filename):
        try:
            os.remove(excel_filename)
        except WindowsError:
            sys.stderr.write("Can't delete the excel file\n")
            sys.exit(1)
            
    
    excel = _ExcelApi.OpenPyExcel(excel_filename)
    
    if not excel.load_workbook():
        sys.stderr.write("Load excel failure\n")
        sys.exit(1)
    
    ws_name = u"新加sheet"
    if excel.add_sheet(ws_name):
        excel.active_sheet = ws_name
    else:
        print "Can't create sheet"
        sys.exit(1)
        
    print "Sheets:", excel.get_sheet_names()
    excel.rename_sheet(u"新加sheet", "test_renamenewname")
    print "New Sheets:", excel.get_sheet_names()
    
    #if not excel.open_sheet("test"):
    #    sys.stderr.write("open sheet failure\n")
    #    sys.exit(1)
    excel.write_cell(1, 1, "hello excel1")
    excel.write_cell(2, 2, "123456")
    excel.write_cell(3, 3, "hello excel3")
    excel.write_cell(4, 4, "hello excel4")
    excel.write_cell_by_coordinate('E5', "hello excel5")
    excel.write_cell_number(6, 6, 123456)
    print "cell 1 1: ", excel.get_cell_value(1, 1)
    print "cell 2 2: ", excel.get_cell_value(2, 2)
    print "cell 3 3 C3: ", excel.get_cell_value_by_coordinate('c3')
    print "cell 5 5 E5: ", excel.get_cell_value(5, 5)
    
    print "rows: ", excel.rows
    print "columns: ", excel.columns
    
    print "Active Sheet: ", excel.active_sheet
    
    
    excel.close()
    