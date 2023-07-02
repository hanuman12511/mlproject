import pandas as pd
import  os
import Graph as g
import DataOperations as do
class DataRead:
    def datacvs(s,list1):
        while(True):
            print("**********************************")
            print(list1)
            filename =int(input("Select file.. enter [0]index =>0 & [1] index =>1/ ect.. "))
            if( filename<len(list1)):
                path = os.getcwd()+"/"+list1[filename]
                df = pd.read_csv(path)
                print(df.columns.values)
                dataop = do.DataOperation()
                year, sell =dataop.getData(df)
                graph =g.Graph()
                while True:
                    gnum= int(input("1 Line Graph\n2 Bar graphs\n3 Pie Chart\n4  Histogram\n5 Scatter plot"))
                    if gnum==1:
                        graph.LineGp(daat)
                    elif gnum==2:
                        graph.BarGp(year,sell)
                    elif gnum==3:
                        graph.PieChartGp(daat)
                    elif gnum==4:
                        graph.HistogramGp(daat)
                    elif gnum==5:
                        graph.ScatterplotGp(daat)
                    else:
                        break
            else :
                print("enter right file index..")
                input()
            