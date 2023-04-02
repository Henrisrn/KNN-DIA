import sys
import pandas as pd
import math
import numpy as np
#Initialisation de valeur
allLabels = ['0','1','2','3']
nbLines = 2000
nneigborgh = 3


#Création de la dataframe à partir d'un fichier txt
dataframe = pd.read_csv(sys.argv[1],sep=";")
dataframe.columns = ["a","b","c","d","e","f","g","allLabels"]
dataframe.to_excel("Entreeoffici.xlsx")
dataframe = pd.read_excel("Entree.xlsx")
test = pd.read_excel("Entre2.xlsx")
print(test)
#Calcul de la longeur à partir des valeurs d'initialisation

for j in range(len(test)):
    distance = []
    for i in range(len(dataframe)):
            distance.append(math.sqrt((float(dataframe['a'][i])-float(test['a'][j]))**2 + (float(dataframe['b'][i])-float(test['b'][j]))**2 + (float(dataframe['c'][i])-float(test['c'][j]))**2 + (float(dataframe['d'][i])-float(test['d'][j]))**2 + (float(dataframe['e'][i])-float(test['e'][j]))**2 + (float(dataframe['f'][i])-float(test['f'][j]))**2 + (float(dataframe['g'][i])-float(test['g'][j]))**2 ))
    dataframe['Calcul'] = distance
    typee = []
    for i in range(nneigborgh):
        ligneplusproche = dataframe[dataframe['Calcul'] == min(dataframe['Calcul'])]
        test["Class"][j] = ligneplusproche['allLabels'].values[0]
        typee.append(test['Class'])
        dataframe['Calcul'].drop(min(dataframe['Calcul']))
    


#Affichage de conclusion
dataframe.to_excel("Sortie1.xlsx")
test.to_excel("Sortie2.xlsx")
print('La class de notre fleur la plus proche est ',str(ligneplusproche['allLabels'].values[0]))
