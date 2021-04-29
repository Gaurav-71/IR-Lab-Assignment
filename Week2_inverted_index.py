import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
import import_ipynb
import Week1_preprocessing_document
import pickle


text = []
document_lengths = []
print('\nPreprocessing Documents...')
for f in range(1, 11):
    tx = Week1_preprocessing_document.preprocess_document("./Inverted Index/T" + str(f) + ".txt")
    text_tokens = word_tokenize(tx)
    document_lengths.append(len(text_tokens))
    text.append(text_tokens)
print('Done\n')


from collections import defaultdict
# initial_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, }

def create_index (data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            if(index[token]):
                index[token][0][0] = index[token][0][0] + 1
                if i in index[token][1].keys():
                    index[token][1][i] = index[token][1][i] + 1
                else:
                    index[token][1][i] = 1
            else:
                index[token] = [[1], {i : 1}]
            
    return index


index = create_index(text)

print('Index of percept -', index['percept'], '\n')

with open('vocabulary', 'wb') as fp:
    pickle.dump(list(index.keys()), fp)

with open('index', 'wb') as fp:
    pickle.dump(index, fp)

print('Document lengths are -',document_lengths, '\n')

with open('document_lengths', 'wb') as fp:
    pickle.dump(document_lengths, fp)

print('Length of the index is -',len(index), '\n')

print('All the index keys are -',index.keys(), '\n')