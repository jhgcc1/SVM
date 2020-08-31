
from sklearn.feature_extraction.text import TfidfVectorizer
def generate_sparse_matrix(docs):
    tfidf = TfidfVectorizer(ngram_range=(1,2)) 
    csr_mat = tfidf.fit_transform(docs)
    features=tfidf.get_feature_names()
    return csr_mat,features