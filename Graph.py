from matplotlib import pyplot as plt  
class Graph:
    def LineGp(s,data):
        print("************  Line Graph ********************  ")
        plt.plot(data)  
        plt.show()  
    def BarGp(s,year,sell):
        print("************  Bar Graph ********************  ")
        players = ['Virat','Rohit','Shikhar','Hardik']  
        runs = [51,87,45,67]  
        plt.bar(year,sell,color = 'green')  
        plt.title('Score Card')  
        plt.xlabel('Players')  
        plt.ylabel('Runs')  
        plt.show()  
                
    def PieChartGp(s,data):
        print("************  PieChart Graph ********************  ")
        Players = 'Rohit', 'Virat', 'Shikhar', 'Yuvraj'  
        Runs = [45, 30, 15, 10]  
        explode = (0.1, 0, 0, 0)  # it "explode" the 1st slice   
        
        fig1, ax1 = plt.subplots()  
        ax1.pie(Runs, explode=explode, labels=Players, autopct='%1.1f%%',  
                shadow=True, startangle=90)  
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.  
        
        plt.show() 
                
    def HistogramGp(s):
        print("************  Histogram Graph ********************  ")
        population_age = [21,53,60,49,25,27,30,42,40,1,2,102,95,8,15,105,70,65,55,70,75,60,52,44,43,42,45]  
        bins = [0,10,20,30,40,50,60,70,80,90,100]  
        plt.hist(population_age, bins, histtype='bar', rwidth=0.8)  
        plt.xlabel('age groups')  
        plt.ylabel('Number of people')  
        plt.title('Histogram')  
        plt.show()  
    def ScatterplotGp(s):
        print("************  Scatterplot Graph ********************  ")
        x = [5,7,10]  
        y = [18,10,6]  
        
        x2 = [6,9,11]  
        y2 = [7,14,17]  
        
        plt.scatter(x, y)  
        
        plt.scatter(x2, y2, color='g')  
        
        plt.title('Epic Info')  
        plt.ylabel('Y axis')  
        plt.xlabel('X axis')  
        
        plt.show() 
