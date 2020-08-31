import pandas as pd
def Generate_list(path):
    df=pd.read_excel(path)
    listOfMovies=df.values.tolist()
    urls=[]
    names=[]
    for item in listOfMovies:
        names.append(item[0])
        name=item[0].replace(" ","%20")
        url= "http://www.omdbapi.com/?t="+name+"&plot=full&apikey=8f16e01a"
        urls.append(url)
    return urls,names
