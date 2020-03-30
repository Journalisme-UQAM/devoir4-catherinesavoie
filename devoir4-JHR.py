# devoir4

### BONJOUR CATHERINE
### TOUT D'ABORD, TON SCRIPT N'ÉTAIT PAS DANS UN FICHIER .PY

### CETTE LIGNE CI-DESSOUS N'ÉTAIT PAS EN COMMENTAIRE...
# remise du devoir 4

### CETTE LIGNE NON PLUS...
# coding utf-8

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

# analyse = "martino.csv"
analyse = "../martino.csv" ### JE CHANGE SIMPLEMENT LE CHEMIN DU FICHIER POUR POUVOIR LE CHARGER SUR MON ORDI

# faire opérer la lecture du fichier 

c = open(analyse)
manipulations = csv.reader(c)
next(manipulations)

# for inter in manipulations ### IL MANQUE QUELQUE CHOSE DE FONDAMENTAL POUR QUE CETTE BOUCLE FONCTIONNE, LE CODE CORRECT EST À LA LIGNE SUIVANTE
for inter in manipulations:

# tokens = word_tokenize(inter[50]) ### IL FAUT INDENTER CETTE LIGNE ET TOUTES CELLES QUI SUIVENT (OU PRESQUE); PAR AILLEURS, CE N'EST PAS L'ÉLÉMENT 50 QUI EST LE BON, MAIS L'ÉLÉMENT 3...
	tokens = word_tokenize(inter[3]) ### IL FAUT INDENTER CETTE LIGNE

# aller à la racine 

	### IL FALLAIT INDENTER CE BLOC
	fr = SnowballStemmer('french')
	# racines = [fr.stem(mot)for mot in word_tokenize(inter[50])] ### LA SYNTAXE DE CETTE LIGNE EST À AMÉLIORER AINSI:
	racines = [fr.stem(mot) for mot in tokens] 
	# print(racines)

	### C'EST BIEN, TU TENTES DE RETRANCHER LES MOTS VIDES
	# tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french')]
	# print(tokens)

	# # retranchement de la ponctuation 
	### MAIS C'EST MIEUX DE RETRANCHER EN MÊME TEMPS LA PONCTUATION
	# tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]
	### ET C'EST ENCORE MIEUX DE LE FAIRE AVEC LE CODE SUIVANT:
	tokens = [mot for mot in tokens if mot not in stopwords.words('french') and mot not in string.punctuation]
	print(tokens)
	print("🌈"*10)

	### POUR LA SUITE DE TON CODE, JE VAIS TE RÉFÉRER À LA SOLUTION QUE JE VAIS METTRE DANS LE SYLLABUS.
	### MALHEUREUSEMENT, CE QUE TU M'AS REMIS ME DONNE L'IMPRESSION QUE TU N'AS JAMAIS TENTÉ DE LE FAIRE FONCTIONNER DANS TON TERMINAL...

# # calculer le nombre de fréquence par mot 

# mots = [fr.stem(mot)for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]

# print(mots)

# # boucle pour le mot islam 

# for mot in mots: 
#     "islam".append(mot)

# freq = Counter("islam")

# freq = Counter("islam")
# print(freq.most_common(50))
# print(len("islam"))

# # boucle pour le mot musulman 

# for mot in mots: 
#     "musulm".append(mot)

# freq = Counter("musulm")

# freq = Counter("musulm")
# print(freq.most_common(50))
# print(len("musulm"))