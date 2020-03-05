import pandas as pd
import numpy as np

n = len(open('lyrics_2013.txt').readlines(  ))
x = np.zeros((n,50))
options = ['bottles','vodka', 'alcohol','beer','hennessey','marijuana','weed',
'kush','cocaine','coke','heroin','crack','heroin','hallucinogens', 'LSD', 'PCP'
,'ecstasy','inhalants','methamphatamine','opiates','amphetamines',
'tranquilizers', 'benzo']

drug_list = []

important_words = ['fun','lit','party','dope','expensive',
'high','hype','illegal','overdose','dead','danger','addictive','use','powerful']

drug_scores = {}

na = 0
with open('vectors.txt', 'r') as file:
    for _ in range(23571):
        line = file.readline()
        for i in range(0,len(line)):
            if line[i] == ' ':
                y = i
                break
        line = line.split()
        if line[0] in options:
            drug_list.append(line[0])
            for i in range(1,len(line)):
                x[na,i-1] = float(line[i])
            na += 1

x = pd.DataFrame(data = x[:na,:])

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
principalDf.to_csv('pca.csv',index=False)
print(drug_list)
