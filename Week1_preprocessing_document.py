import os
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

show_statistics = True

def preprocess_document(fname):
    
    doc = open(fname, encoding='iso-8859-1')
    num_words=0

    x = ""

    for line in doc:
        split_line = line.split(" ")
        num_words+=len(split_line)

        line = ''.join(e for e in line if e.isalnum() or e == ' ')

        line = line + "\n"
        x = x + line


    text_tokens = word_tokenize(x)
    tokens_without_stopwords = [
        word for word in text_tokens if word not in stopwords.words()]


    porter_stemmer = PorterStemmer()

    final_text = ""
    for t in tokens_without_stopwords:
        final_text = final_text + porter_stemmer.stem(t) + " "

    if(show_statistics):

        s1 = os.path.getsize(fname)

        f = open("temp.txt", "w")
        f.truncate(0)
        f.write(x)
        f.close()
        s2 = os.path.getsize("temp.txt")
        
        f = open("temp.txt", "w")
        f.truncate(0)
        f.write(" ".join(tokens_without_stopwords))
        f.close()
        s3 = os.stat("temp.txt").st_size
        
        f = open("temp.txt", "w")
        f.truncate(0)
        f.write(final_text)
        f.close()
        s4 = os.path.getsize("temp.txt")
        
        print("\nSize of Document before processing -",  s1, "bytes")
        print("Size of Document after lexical analysis -", s2, "bytes")
        print("Size of Document after stopwords removal -", s3, "bytes")
        print("Size of Document after stemming -", s4, "bytes")
        print("Percentage decrease in size - ", str(round(100*((s1 - s4)/s1), 2))+'%')

    print("Finished preprocessing -", fname)

    return final_text


def preprocess_query(query):
    line = query

    line = ''.join(e for e in line if e.isalnum() or e == ' ')

    text_tokens = word_tokenize(line)
    tokens_without_stopwords = [
        word for word in text_tokens if not word in stopwords.words()]

    x = ""
    for token in tokens_without_stopwords:
        x = x + token + " "

    porter_stemmer = PorterStemmer()

    text_tokens = word_tokenize(x)

    final_text = ""
    for w in text_tokens:
        final_text = final_text + porter_stemmer.stem(w) + " "

    return final_text


def main():

    for i in range(1, 4):

        preprocessed_doc = preprocess_document(
            "./Document Preprocessing/Text"+str(i)+".txt")
        f = open('./Document Preprocessing/PreprocessedText'+str(i)+'.txt', 'w')
        f.write(preprocessed_doc)
        f.close()

if(show_statistics):
    main()
    print()

