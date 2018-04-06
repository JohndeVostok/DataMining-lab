import pickle
from wordcloud import WordCloud

with open("attr.pkl", "rb") as f:
    attrList = pickle.load(f)

# Wordcloud

wordList = []

for i in attrList:
    for j in i["stems"]:
        wordList.append(j)

text = ' '.join(wordList)

with open("fullText.txt", "w") as f:
    f.write(text)

wc = WordCloud(background_color = 'white', scale = 1.5).generate(text)
wc.to_file('wordcloud.jpg')
