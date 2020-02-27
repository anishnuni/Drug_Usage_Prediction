import pandas as pd

df = pd.read_csv("lyrics.csv")

file1 = open("lyrics_2011.txt","a")
x = df.shape[0]
n=0
for i in range(df.shape[0]):
    if type(df['lyrics'][i]) == type('lyric') and df['year'][i] == 2011:
        y = df['lyrics'][i].splitlines()
        lyrics = ' '
        for lyric in y:
            lyrics = lyrics + lyric + ' '
        n+=1
        file1.write(lyrics)
        file1.write('\n')
    print(n, i/x)
