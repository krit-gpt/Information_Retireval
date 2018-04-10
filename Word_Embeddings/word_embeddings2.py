import nltk
nltk.download('brown')

from nltk.corpus import brown
brown.words()
# Your Code Here...
'''
Removing the stopwords using the stopwords from 3 libraries -- 
1. nltk
2. sklearn
3. spacy

- Removing blank spaces, numbers and '$'
'''

from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from spacy.lang.en import STOP_WORDS as STOPWORDS
import re
import operator

stop = set(stopwords.words('english') + list(string.punctuation) + ['the'] + ["''"] + ["``"] + list('1234567890'))
stop.add(ENGLISH_STOP_WORDS)
stop.union(STOPWORDS)

data = []

#[i for i in word_tokenize(sent.lower()) if i not in stop]
dict_word = {}
digits = ['1','2','3','4','5','6','7','8','9','0', '$', '-', '/', '.']
digits_set = set(digits)
data = []
for word in brown.words():
    data.append(word)
    if word.lower() not in stop:
        if word[0] not in digits_set:  #removing digits
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
            
i = 0
dict_word = sorted(dict_word.items(), key = lambda x:x[1], reverse=True)
print(dict_word[:20])



import unicodedata

context = set()
vocab = set()
context_dict = {}
vocab_dict = {}
i = 0
for w in dict_word[:1000]:
        first =  w[0]
        second = unicodedata.normalize('NFKD', first).encode('ascii','ignore')
        context_dict[str(second)] = i
        i += 1
        context.add(w[0])

i = 0
for w in dict_word[:5000]:
    first = w[0]
    second = unicodedata.normalize('NFKD', first).encode('ascii','ignore')
    vocab_dict[str(second)] = i
    i += 1
    vocab.add(w[0])


    # Your Code Here...
cooc_matrix = []

for word in vocab:
    temp = []
    for cont in context:
        temp.append(0)
    cooc_matrix.append(temp)
#print(len(cooc_matrix))

#initializes a 5000x1000 matrix

# need to map each vocab word with a number and each context word with a number
# given in the above cell


i = 0
# data = data[:500]
matrix_sum = 0

for word in data:
    ind = i
    if word.lower() in vocab:
        matrix_v_ind = vocab_dict[word.lower()]
        window = data[ind-2:ind+3]
        #print(window)
        for j in window:
            if j.lower() in context:
                #print("yo!")
                matrix_sum += 1
                matrix_c_ind = context_dict[j.lower()]
                cooc_matrix[matrix_v_ind][matrix_c_ind] += 1
    i += 1
#print(cooc_matrix[:20][:20]) 
print("Number of times the condition meet is:")
print(total2)
print("")


matrix_sum = 0

for row in range(len(cooc_matrix)):
    for col in range(len(cooc_matrix[0])):
        matrix_sum += cooc_matrix[row][col]
print(matrix_sum)

# Your Code Here...
# As far as I understood the question, Pr(c|w) = element/row_sum, and Pr(c) = Column_sum/matrix_sum

pr_matrix = []

for row in range(len(cooc_matrix)):
    temp = []
    for col in range(len(cooc_matrix[0])):
        temp.append(0)
    pr_matrix.append(temp)

row_sum = 0

for row in range(len(cooc_matrix)):
    row_sum = sum(cooc_matrix[row])
    #print(row_sum)
    for col in range(len(cooc_matrix[0])):
        if row_sum != 0:
            pr_matrix[row][col] = (cooc_matrix[row][col])/float(row_sum)
        else:
            pr_matrix[row][col] = 0

# for i in range(len(pr_matrix)):
#     for j in range(len(pr_matrix[0])):
#         if pr_matrix[i][j] < 0:
#             print(pr_matrix[i][j])


#print(pr_matrix[:20][:20])


#new block   
col_sum = [0]*len(cooc_matrix[0])

for row in range(len(cooc_matrix)):
    for col in range(len(cooc_matrix[0])):
        col_sum[col] += cooc_matrix[row][col]
print(col_sum[:20])
#print(len(col_sum))

pr_c = [0]*1000
# total = 0
for i in range(len(col_sum)):
    pr_c[i] = (col_sum[i]/float(matrix_sum))
#     if pr_c[i] < 0:
#         total += 1
# print(total)
print(pr_c[:20])



# Your Code Here...
import math

print(len(pr_matrix[0]))
vector_matrix = []

for row in range(len(pr_matrix)):
    temp = []
    for col in range(len(pr_matrix[0])):
        if int(pr_c[col]) != 0:
            #temp.append(max(0, math.log(pr_matrix[row][col]/(pr_c[col]))))
            #print(math.log(pr_matrix[row][col]/(pr_c[col])))
            print(pr_matrix[row][col]/float(pr_c[col]))
            #print("uokdv")
        else:
            print("ghghghghghgh")
            #temp.append(0)
            #print(0)
    #vector_matrix.append(temp)
#print(vector_matrix[:20])
        
