import pickle
import Week1_preprocessing_document
from nltk.tokenize import word_tokenize
import numpy as np

index = None
vocabulary = None
document_lengths = None
with open('vocabulary', 'rb') as fp:
    vocabulary = pickle.load(fp)
with open('index', 'rb') as fp:
    index = pickle.load(fp)
with open('document_lengths', 'rb') as fp:
    document_lengths = pickle.load(fp)

print("Index ['project'] : ",index['project'])

n_vec = np.zeros(len(vocabulary)) # net vector storing net ratio for all the words 

for key in index:
    term = index[key]
    nw = len(term[1].keys())
    net = (10 - nw + 0.5)/(nw + 0.5)
    i = vocabulary.index(key)
    n_vec[i] = net


query = "A somewhat higher level on the inclined plane is illustrated by what are called tropisms obligatory movements which the animal makes, adjusting its whole body so that physiological equilibrium results in relation to gravity, pressure, currents, moisture, heat, light, electricity, and surfaces of contact. A moth is flying past a candle; the eye next the light is more illumined than the other; a physiological inequilibrium results, affecting nerve-cells and muscle-cells; the outcome is that the moth automatically adjusts its flight so that both eyes become equally illumined; in doing this it often flies into the candle."
query = Week1_preprocessing_document.preprocess_query(query) 
query = word_tokenize(query)

ranking = []

for i in range(0, 10): # initializing same rank for all docs
    ranking.append([1, i+1])

for key in query: # key is tokenized word
    term = index[key] # tokenized word dictionary value
    i = vocabulary.index(key) # position of tokenized word in vocab
    net = n_vec[i] # net ratio of tokenized word
    for doc_num in term[1].keys(): # loop to fetch document numbers and ranking ( done based on net ratio value )
        ranking[doc_num][0] = ranking[doc_num][0]*net

ranking.sort(reverse=True)
print("Ranking : ",ranking)

