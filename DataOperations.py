class DataOperation:
    def getData(s,df):
        print(df)
        while True:
            print("*****************")
            gpby = df.groupby('Year')['Selling_Price'].sum().reset_index()
            print(gpby)
            year=gpby.loc[:,'Year']
            sell=gpby.loc[:,'Selling_Price']
            return (year,sell)
            input()