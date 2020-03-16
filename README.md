# devoir4
remise du devoir 4 

coding utf-8

# faire afficher les 50 paires de mots qui se trouvent le plus souvent dans les chronique de Richard Martineau. 

import csv 

# pour calculer la fréquence 
from collections import Counter 

import nltk 

# pour la punctuation 
import string 

# pour tokeniser les éléments 
from nltk.tokenize import word_tokenize

# afin d'aller à la racine des mots 
from nltk.stem import SnowballStemmer 

# pour le travail des mots vides 
from nltk.corpus import stopwords

# ajouter mon fichier CSV 

analyse = "martino.csv"

# faire opérer la lecture du fichier 

c = open(analyse)

manipulations = csv.reader(c)

next(manipulations)

for inter in manipulations

tokens = word_tokenize(inter[50])

# aller à la racine 

fr = SnowballStemmer('french')
racines = [fr.stem(mot)for mot in word_tokenize(inter[50])]
print(racines)

tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french')]

print(tokens)

# retranchement de la ponctuation 

tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]

print(tokens)

# calculer le nombre de fréquence par mot 

mots = [fr.stem(mot)for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]

print(mots)

# boucle pour le mot islam 

for mot in mots: 
    "islam".append(mot)

freq = Counter("islam")

freq = Counter("islam")
print(freq.most_common(50))
print(len("islam"))

# boucle pour le mot musulman 

for mot in mots: 
    "musulm".append(mot)

freq = Counter("musulm")

freq = Counter("musulm")
print(freq.most_common(50))
print(len("musulm"))
