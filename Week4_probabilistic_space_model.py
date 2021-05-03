import pickle
import Week1_preprocessing_document
from nltk.tokenize import word_tokenize
import numpy as np

def print_ranks(ranking):
    print("Document Number \t Rank")
    print("--------------------------------------------------")
    for pair in ranking:
        print("\t",pair[1],"\t\t",pair[0])
    print()

index = None
vocabulary = None
document_lengths = None
with open('vocabulary', 'rb') as fp:
    vocabulary = pickle.load(fp)
with open('index', 'rb') as fp:
    index = pickle.load(fp)
with open('document_lengths', 'rb') as fp:
    document_lengths = pickle.load(fp)

print('Ready for ranking the query -')

n_vec = np.zeros(len(vocabulary)) # net vector storing net ratio for all the words 

for key in index:
    term = index[key]
    nw = len(term[1].keys())
    net = (10 - nw + 0.5)/(nw + 0.5)
    i = vocabulary.index(key)
    n_vec[i] = net


query = input("\nEnter your query :") 
query = Week1_preprocessing_document.preprocess_query(query) 
query = word_tokenize(query)

print(index['sun'])
print(index['moon'])
ranking = []

for i in range(0, 10): # initializing same rank for all docs
    ranking.append([1, i+1])

for key in query: # key is tokenized word
    term = index[key] # tokenized word dictionary value
    i = vocabulary.index(key) # position of tokenized word in vocab
    net = n_vec[i] # net ratio of tokenized word
    for doc_num in term[1].keys(): # loop to fetch document numbers and ranking ( done based on net ratio value )
        ranking[doc_num][0] *= (net)

print("\nRanking of the documents w.r.t the query --\n")
ranking.sort(reverse=True)
print_ranks(ranking)


