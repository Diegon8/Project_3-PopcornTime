def removeNaN(x, y):
    return x[y.notna()].reset_index(drop=True)

def decader(x):
    return (x//10)*10

def dollar_to_int(x):
    return x.str.replace('$','').str.replace(' ','').astype('int64')

def create_table(x, y):
    x= round((df.groupby(y).agg({'budget':['max','mean'],"worlwide_gross_income":['max','mean'],"profit":["max",'mean']}))/1000000 , 0).astype('int64')
    x['profit_ratio']= round(df.groupby(y).agg({"profit_ratio":"mean"}),2)
    x['n_movies']=df.groupby(y).agg({'title':'count'})
    return x