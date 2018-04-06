import os
from datetime import date
import xml.etree.ElementTree as et
import nltk
import re

import pickle

import nltk.stem

rootPath = "nyt_corpus/samples_500/"

def search(node, attrs):
    if (node.tag == "meta"):
        if (node.attrib["name"] == "publication_day_of_month"):
            attrs["date"] = attrs["date"].replace(day = int(node.attrib["content"]))
        if (node.attrib["name"] == "publication_month"):
            attrs["date"] = attrs["date"].replace(month = int(node.attrib["content"]))
        if (node.attrib["name"] == "publication_year"):
            attrs["date"] = attrs["date"].replace(year = int(node.attrib["content"]))
    
    if (node.tag == "block" and node.attrib["class"] == "full_text"):
        attrs["text"] = ""
        for i in node:
            attrs["text"] = attrs["text"] + " " + i.text
        return

    if (node.tag == "classifier"):
        nodeType = node.text;
        wordList = nodeType.split('/')
        if (len(wordList) > 2 and wordList[0] == "Top" and (wordList[1] == "News" or wordList[1] == "Features")):
            flag = 0
            for i in attrs["tags"]:
                if i == wordList[2]:
                    flag = 1
            if (not flag):
                attrs["tags"].append(wordList[2])
    for i in node:
        search(i, attrs)


if (__name__ == "__main__"):
    fileList = os.listdir(rootPath)
    attrList = []
    for fileName in fileList:
        filePath = os.path.join(rootPath, fileName)
        tree = et.parse(filePath)
        root = tree.getroot()
        attrList.append({})
        attrs = attrList[len(attrList) - 1]
        attrs["date"] = date(2000, 12, 31)
        attrs["text"] = ""
        attrs["tags"] = []
        search(root, attrs)

        tokens = [word for sent in nltk.sent_tokenize(attrs["text"]) for word in nltk.word_tokenize(sent)]
        filteredTokens = []
        for token in tokens:
            if re.search("[a-zA-Z]", token):
                filteredTokens.append(re.sub("[^a-zA-Z]", "", token))

        stemmer = nltk.stem.SnowballStemmer('english')
        stems = [stemmer.stem(t) for t in filteredTokens]
        attrs["stems"] = stems

with open("attr.pkl", "wb") as f:
    pickle.dump(attrList, f)
