import pandas as pd
import  os
class DataRead:
    def datacvs(s,list1):
        while(True):
            print(os.getcwd())
            path = os.getcwd()+"/"+list1[0]
            print(path)
            df = pd.read_csv(path)
            print(df)
            input()
            