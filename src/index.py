# Used common elements of NLP to determine scientific terminology/taxonomic data
# Dataset is obtained from PDF, preprocessed using libraries of NLP

#Packages used - PyPDF, NLTK, pandas, scikit-learn, re

#importing packages
from os import read
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
import PyPDF2

from clean import *

with open('./assets/ribosome_sample.pdf', mode='rb') as file_, open('./assets/ribosome_sample.txt', 'w', encoding='utf-8') as text_file:
    read_pdf = PyPDF2.PdfFileReader(file_)
    # print(read_pdf)
    num_pages = read_pdf.numPages
    for pg in range(num_pages):
        pageObject = read_pdf.getPage(pg)
        text_file.write(pageObject.extractText())
    file_.close()
    
with open('./assets/ribosome_sample.txt', 'r', encoding="latin-1") as f:
    read_output = f.readlines()

read_output = '\n'.join(read_output).strip().replace('\n','')

# print(read_output)

#Preprocessing or cleaning
# Removing digits, stopwords, words less than 3 char long, and punctuation usign re
# Adding to that a customized list of scientific words, not related to this analysis will also be removed

pdf_o = clean_text(read_output)
# print(pdf_o)
text_tokens = word_tokenize(pdf_o)

pdf_i = [pdf_o]

# Obtaining bigrams and tigrams
vectorizer = CountVectorizer(ngram_range= (2, 3))
X1 = vectorizer.fit_transform(pdf_i)
features = (vectorizer.get_feature_names())

X2 = vectorizer.fit_transform(pdf_i)
scores = (X2.toarray())

sums = X2.sum(axis=0)
data1 = []

for col, term in enumerate(features):
    data1.append( (term, sums[0, col]) )

ranking = pd.DataFrame(data1, columns=['term', 'rank'])
words = (ranking.sort_values('rank', ascending=False))
print("\n\nWords : \n", words.head(50))

