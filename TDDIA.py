import pandas as pd
import math
import numpy as np
"""Sepallenght = float(input())
SepalWidth = float(input())
PetalLenght = float(input())
PetalWidth = float(input())"""
def Calculdelamoyenne(table):
    sum = 0
    print(table)
    for i in table:
        sum+=float(i)
    return sum/len(table)
Sepallenght = 2.4
SepalWidth = 2.5
PetalLenght = 5.6
PetalWidth = 0.7
file = open('IA3-ml_data_iris.txt','r')
data = file.readlines()
dataframe = []
for i in data:
    word = i.split(",")
    a = []
    for j in word:
        if "\n" in j:
            j = j.replace('\n','')
        a.append(j)
    dataframe.append(a)
    
dataframe = pd.DataFrame(dataframe) 
dataframe.columns =['Sepal Length', 'Sepal Width', 'Petal Lenght', 'Petal Width','Class']
df_aleatoire = dataframe.sample(n=len(dataframe) // 2)
print(df_aleatoire)
nomclass = dataframe['Class'].unique()
nomclass = list(set(dataframe['Class']))
selected_rows_setosa = dataframe[dataframe['Class'] == nomclass[2]]
selected_rows_versicolor = dataframe[dataframe['Class'] == nomclass[1]]
selected_rows_virginica = dataframe[dataframe['Class'] == nomclass[0]]
moyenne = []
for j in nomclass:
    for i in dataframe.columns:
        if(i != 'Class'):
            moyenne.append(Calculdelamoyenne(dataframe[dataframe['Class'] == j][i]))
distance = []
for i in range(len(dataframe)):
        distance.append(math.sqrt((float(dataframe['Sepal Length'][i])-float(Sepallenght))**2 + (float(dataframe['Sepal Width'][i])-float(SepalWidth))**2 + (float(dataframe['Petal Lenght'][i])-float(PetalLenght))**2 + (float(dataframe['Petal Width'][i])-float(PetalWidth))**2))
dataframe['Calcul'] = distance
ligneplusproche = dataframe[dataframe['Calcul'] == min(dataframe['Calcul'])]
print('La class de notre fleur la plus proche est ',str(ligneplusproche['Class'].values[0]))
"""for j in dataframe.columns:
    if j!='Class':
        moyenne.append(dataframe[j].mean)
        moyenne.append(j)
        medianne.append(dataframe[j].median)
        medianne.append(j)
    for i in range(len(dataframe)):
        data = dataframe[j][i]
print(moyenne)
print(medianne)"""