import os
import pandas as pd
listcsv=[]
class SystemOs:
    def changeDir(self,path):
        dir = os.chdir(path)
        
    def getCurDir(self):
        while True:
            print(os.getcwd())
            entries = os.listdir(os.getcwd())
            ch = int(input("1.print all file &dir \n2 for get csv file"))
            if ch==1:
                for i in entries:
                    print(i)
            elif ch ==2:
                
                for i in entries:
                    split_tup = os.path.splitext(i)
                    if(split_tup[1]==".csv"):
                        print(i)
                        listcsv.append(i)
                print(listcsv)
                print(listcsv[0])
                return listcsv
               
                    
            else:
                break    
            