import pandas as pd
import numpy as np

n = len(open('lyrics_2013.txt').readlines())
x = np.zeros((n, 50))
options = ['bottles', 'vodka', 'alcohol', 'beer', 'hennessey', 'marijuana', 'weed',
           'kush', 'cocaine', 'coke', 'heroin', 'crack', 'heroin', 'hallucinogens', 'LSD', 'PCP',
           'ecstasy', 'inhalants', 'methamphatamine', 'opiates', 'amphetamines', 'tranquilizers', 'benzo']

drug_list = []

important_words = ['fun', 'lit', 'party', 'dope', 'expensive',
                   'high', 'hype', 'illegal', 'overdose', 'dead', 'danger', 'addictive', 'use', 'powerful']
not_found = important_words[:]
important_word_vectors = {}

# adds the important word vectors to the important_word_vectors_dictionary

with open('vectors.txt', 'r') as file:
    for _ in range(n):
        line = file.readline().split()
        if line[0] in not_found:
            not_found.remove(line[0])
            vec = []
            for i in range(1, len(line)):
                vec.append(float(line[i]))
            important_word_vectors[line[0]] = vec

drug_scores = {}
drug_n_occurences = {}

with open('vectors.txt', 'r') as file:
    for _ in range(n):
        line = file.readline().split()
        if line[0] in options:



na = 0
with open('vectors.txt', 'r') as file:
    for _ in range(23571):
        line = file.readline()
        line = line.split()
        if line[0] in options:
            drug_list.append(line[0])
            for i in range(1, len(line)):
                x[na, i - 1] = float(line[i])
            na += 1

x = pd.DataFrame(data=x[:na, :])

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents
                           , columns=['principal component 1', 'principal component 2'])
principalDf.to_csv('pca.csv', index=False)
print(drug_list)
