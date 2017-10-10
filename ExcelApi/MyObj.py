# -*- coding: cp936 -*-

import traceback, sys, inspect


class MyObj(object):
    def __init__(self):
        super(MyObj, self).__init__()
        
    def trace_err(self):
        (exc_type, exc_val, exc_tb) = sys.exc_info()
        formatted_lines = traceback.format_exception(exc_type, exc_val, exc_tb)
        err = formatted_lines[-1].split(':')
        if len(err) <= 1:
            return err[0]
        else:
            return err[1]

    def get_func_name(self):
        (_, _, _, func_name, _, _) = inspect.stack()[1]
        return func_name
    
    def dump_class(self):
        instance = ''
        module = self.__class__.__name__
        sys.stdout.write("\n<Instance \"%s\" - %s Module:\n" %(instance, module))
        for attr in self.__dict__:
            sys.stdout.write("    %-10s:  "%str(attr))
            (_, attr_type) = self.get_var_type(self.__dict__[attr])
            if attr_type == "dict":
                print ""
            for key in self.__dict__[attr].keys():
                    print "      ", key, " = ", self.__dict__[attr][key]
            else:
                print self.__dict__[attr]
        sys.stdout.write("End Instance \"%s\" - %s Module>\n\n" %(instance, module))
        
        
        
        
        