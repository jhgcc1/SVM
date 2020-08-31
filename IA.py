
import requests
from IA_read_excel import Generate_list
import json
from sparse import generate_sparse_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
import re
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
import nltk
from sklearn.svm import SVC
nltk.download('stopwords')
from nltk.corpus import stopwords

stop=set(stopwords.words('english'))
print(stop)
docs=[]
genreList=[]
Movies,MoviesName=Generate_list(path="C:\\Users\\CavalcantiJ\\Desktop\\IA\\Book1.xlsx")
for movie in Movies:
    response=requests.get(movie)
    json_data = json.loads(response.text)
    Content=json_data["Plot"].replace("\n"," ").replace("(","").replace(")","").replace("=","").replace("."," ").replace(",","").replace("  "," ").replace("   "," ")
    Content=re.sub(r'[0-9]+','',Content)
    genreList.append(json_data["Genre"].split(",")[0])
    for word in stop:
        Content=Content.replace(" " +word+" "," ")
    Content=Content.replace("  "," ").replace("   "," ")
    docs.append(Content)
    print(movie)

sparse_matrix,features=generate_sparse_matrix(docs)
print(sparse_matrix)
#X_train, X_test, y_train, y_test = train_test_split(sparse_matrix,genreList, test_size=0.95)
svclassifier = SVC(kernel='linear')
svd=TruncatedSVD(n_components=200)
pipeline=make_pipeline(svd,svclassifier)
pipeline.fit(sparse_matrix, genreList)
genre = pipeline.predict(sparse_matrix)
df = pd.DataFrame({'group': genre, 'Movie': MoviesName, "Original group":genreList})
print(df)
df.to_csv(r'C:\\Users\\CavalcantiJ\\Desktop\\IA\\OutputIA.csv')

