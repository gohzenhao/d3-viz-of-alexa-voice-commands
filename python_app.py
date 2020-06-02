import pandas as pd
import numpy as np
import json
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

# Store common words in array
common_words = []
with open("common_words.txt") as f:
    for line in f:
        common_words.append(line.rstrip())
f.close()

# Read data in json format 
data = pd.read_excel(r'C:\Users\gohzenhao\Desktop\COMP7802_research_project\Conference Paper\data_set_1.xlsx')
df = pd.DataFrame(data, columns= ['keyPhrases (S)'])
df2 = pd.DataFrame(data, columns= ['transcript (S)'])

data2 = df.values[0][0]
jsonFormat = json.loads(data2)

print("Key Phrases")

key_phrases = []
for key in jsonFormat:
    split = key['Text'].split(' ')
    for word in split:
        lower = word.lower()
        if lower not in common_words and lower not in key_phrases:
            key_phrases.append(lower)

text = df.values[0][0]
text2 = "What is the weather today?"

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

