import os
import line as l
import SystemOs as s
import dataread as r
obj = s.SystemOs()
           
class mainstart:
    def __init__(self):
        while True:
            ch = int(input("enter choice:\n1.print line\n2.getdir\n3.chnage dir\n"))

            if ch==1:
                l.line()
            elif ch == 2:
                obj.getCurDir()
            elif ch == 3:
                path=input("enter path")
                obj.changeDir(path)
                list1 =obj.getCurDir()
                r.DataRead().datacvs(list1)
d =mainstart()