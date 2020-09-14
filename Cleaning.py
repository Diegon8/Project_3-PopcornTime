def removeNaN(x, y):
    return x[y.notna()].reset_index(drop=True)

def decader(x):
    return (x//10)*10

def dollar_to_int(x):
    return x.str.replace('$','').str.replace(' ','').astype('int64')

