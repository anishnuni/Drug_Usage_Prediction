import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import lyricsgenius



df_test = pd.read_excel("billboard_weekly.xlsx")

print("Loaded billboard charts")

"""
year_count = {}
for i in range(320495):
    year = str(df_test.iloc[i]["WeekID"])[0:4]
    if len(year) == 4:
        try:
            year_count[year] = year_count[year] + 1
        except:
            year_count[year] = 1

x = np.zeros(100)
for i in range(100):
    x[i] = i + 1920

y = np.zeros(100)
for key, value in year_count.items():
    try:
        ind = int(key) - 1920
        y[ind] = value
    except:
        print("Error on key:", key)
print(x)
print(y)
plt.title("Is this enough songs?")
plt.xlabel("Year")
plt.ylabel("Number of Songs")
plt.plot(x,y)
plt.show()
"""
genius = lyricsgenius.Genius("wSdSk17B9i8nwJpoDFJUGowo9KDWDNwDb5ycoZcQE8qTiWQj0r-52nBWUL3x2_kG")
genius.remove_section_headers = True
lyrics_dict = {}

for i in range(320495):
    print("Percent Lyrics Found:", i/320495)
    song_name = str(df_test.iloc[i]["Song"])
    artist = str(df_test.iloc[i]["Performer"])
    first_artist = ""
    year = str(df_test.iloc[i]["WeekID"])[0:4]
    for char in artist:
        if char != ',':
            first_artist = first_artist + char
        else:
            break
    try:
        song = genius.search_song(song_name, first_artist)
        if len(song.lyrics) > 250:
            try:
                lyrics_dict[year] = lyrics_dict[year] + " " + song.lyrics
            except:
                lyrics_dict[year] = song.lyrics
    except:
        print("")
        print("Failed on Song_name:", song_name)
        print("And artist:", first_artist)


i = 0
l = len(lyrics_dict)
for key, value in lyrics_dict.items():
    print("Percent Lyrics Written:", i/l)
    name = 'new_lyrics_' + str(key) + '.txt'
    f = open(name,'wb')
    f.write(value)
    f.close()
    i += 1
