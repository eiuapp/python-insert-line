#!/usr/bin/env python
 
import os
import sys
import fileinput
 
class Insert_line(object):
 
    def __init__(self, file, keyword, newline):
        self.__file = file
        self.__key = keyword
        self.__newline = newline
 
    def _get_specify_lineno(self):
        i = 1
        try:
            f = open("%s" % self.__file)
        except IOError,e:
            print e[1] + ' "%s"' % e.filename
            sys.exit(1)
        while True:
            line = f.readline()
            if not line: break
            if "%s" % self.__key in line:
                return i
                break
            i += 1
        f.close()
 
    def _inserted_newline_list(self):
        if self._get_specify_lineno():
            ls = os.linesep
            f = open("%s" % self.__file)
            li = f.readlines()
            f.close()
            li.insert(self._get_specify_lineno() + 0, self.__newline + ls )
            return li
 
    def inserted_new_file(self):
        if self._inserted_newline_list():
            lines = self._inserted_newline_list()
            os.system("cp %s %s.bak" % (self.__file, self.__file))
            f = open("%s" % self.__file, 'w')
            f.writelines(lines)
            f.close()
        else:
            print 'No such keyword "%s"' % self.__key
 
 
if __name__ == "__main__":
    def _main():
        file = Insert_line("./test/test.txt", "the first line", "the second line")
        file.inserted_new_file()
    _main()