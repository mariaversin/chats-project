from sklearn.metrics.pairwise import cosine_similarity as distance
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def recommender(name,dicc):

    ''' Function to find your best friend '''
    
    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform(dicc.values())
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names(), index=dicc.keys())
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(similarity_matrix, columns=dicc.keys(), index=dicc.keys())
    np.fill_diagonal(sim_df.values, 0) 
    simil = sim_df.idxmax()
    dic={}
    dic[name]= simil.loc[name]
    return dic