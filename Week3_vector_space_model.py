from collections import Counter
import numpy as np
import pickle
#import import_ipynb
import Week1_preprocessing_document
from nltk.tokenize import word_tokenize


index = None
vocabulary = None
document_lengths = None
with open('vocabulary', 'rb') as fp:
    vocabulary = pickle.load(fp)
with open('index', 'rb') as fp:
    index = pickle.load(fp)
with open('document_lengths', 'rb') as fp:
    document_lengths = pickle.load(fp)


tf_matrix = np.zeros((10, len(vocabulary)))


def find_tf():
    for key in index:
        term = index[key]
        for tf in term[1].keys():
            term_freq = term[1][tf]
            i = vocabulary.index(key)
            tf_matrix[tf][i] = term_freq/document_lengths[tf]


find_tf()
print("\n\nTF Matrix -\n\n", tf_matrix)
idf_matrix = np.zeros(len(vocabulary))


def find_idf():
    for key in index:
        term = index[key]
        idf = len(term[1].keys())
        res = np.log10(10/idf)
        i = vocabulary.index(key)
        idf_matrix[i] = res


find_idf()
print("\n\nIDF Matrix -\n\n",idf_matrix)

tf_idf = tf_matrix * idf_matrix
print("\n\nTF * IDF Matrix - \n\n", tf_idf)


def query_tf_idf(query):
    counter = Counter(query)
    word_count = len(query)
    tfm = np.zeros(len(vocabulary))
    idfm = np.zeros(len(vocabulary))
    for token in np.unique(query):
        tf = counter[token]/word_count
        i = vocabulary.index(token)
        idfm = idf_matrix[i]
        tfm[i] = tf
    return(tfm*idfm)


def print_ranks(ranking):
    print("Document Number \t Rank")
    print("--------------------------------------------------")
    for pair in ranking:
        print("\t",pair[1],"\t\t",pair[0])


query = input("\nEnter your query :") 
query = Week1_preprocessing_document.preprocess_query(query)
query = word_tokenize(query)
query_matrix = query_tf_idf(query)

print("\n\nRanking of the documents w.r.t the query --\n")

ranking = []
for i in range(0, 10):
    row = tf_idf[i]
    rank = np.dot(row, np.transpose(query_matrix)) / \
        (np.linalg.norm(row)*np.linalg.norm(query_matrix))
    ranking.append([rank, i + 1])

ranking.sort(reverse=True)
print_ranks(ranking)

print("\n\nRanking of the documents w.r.t T7.txt  --\n")

ranking = []
x_matrix = tf_idf[6]
for i in range(0, 10):
    row = tf_idf[i]
    rank = np.dot(row, np.transpose(x_matrix)) / \
        (np.linalg.norm(row)*np.linalg.norm(x_matrix))
    ranking.append([rank, i+1])

ranking.sort(reverse=True)
print_ranks(ranking)

print("\n")
