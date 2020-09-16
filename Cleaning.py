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

#Calling Image movie API

def requestIMG(code,token = os.getenv('apikey')):
    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    querystring = {"imdb":code,"type":"get-movies-images-by-imdb"}
    headers = {
         'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
         'x-rapidapi-key': token
          }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    imglink =response['poster']
    display(Image(imglink))
