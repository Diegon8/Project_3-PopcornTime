#Remove NaN in column x=dataframe y=column
def removeNaN(x, y):
    return x[y.notna()].reset_index(drop=True)

#transform year into decade x=year
def decader(x):
    return (x//10)*10

#Transform currency str into integer
def dollar_to_int(x):
    return x.str.replace('$','').str.replace(' ','').astype('int64')

#create new summary tables from Dataframe
def create_table(i,x, y):
    x= round((i.groupby(y).agg({'budget':['max','mean'],"worlwide_gross_income":['max','mean'],"profit":["max",'mean']}))/1000000 , 0).astype('int64')
    x['profit_ratio']= round(i.groupby(y).agg({"profit_ratio":"mean"}),2)
    x['n_movies']=i.groupby(y).agg({'title':'count'})
    return x