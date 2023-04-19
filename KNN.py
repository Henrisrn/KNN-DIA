import sys
import pandas as pd
import math
import numpy as np
import datetime as dt
from sklearn.model_selection import train_test_split
#Initialisation de valeur
allLabels = ['0','1','2','3']
nbLines = 2000
nneigborgh = 1
#Creation de la matrice de confusion pour analyser nos resultat
def confusion_matrix(y_true, y_pred):
    matrix = np.zeros((len(allLabels), len(allLabels)))
    for true, pred in zip(y_true, y_pred):
        matrix[int(true), int(pred)] += 1
    return matrix
#creation de rapport des resultats
def classification_report(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    report = "Class\tPrecision\tRecall\tF1-score\n"
    R = 0
    for i in range(len(allLabels)):
        tp = matrix[i, i]
        fp = np.sum(matrix[:, i]) - tp
        fn = np.sum(matrix[i, :]) - tp
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1_score = 2 * (precision * recall) / (precision + recall)
        report += "{}\t{:.2f}\t\t{:.2f}\t{:.2f}\n".format(allLabels[i], precision, recall, f1_score)
    PT=R/len(allLabels)
    print("Precision gobal: "+str(PT)+"%")
    return report
#Création de la dataframe à partir d'un fichier txt
#dataframe = pd.read_csv(sys.argv[1],sep=";")
dataframe = pd.read_csv("ProjetDIA//data.txt",sep=";")
dataframe.columns = ["a","b","c","d","e","f","g","allLabels"]
dataframe.to_excel("ProjetDIA//Entreeoffici.xlsx")
print(len(dataframe))
deuxiemedata = pd.read_csv("ProjetDIA//preTest.txt",sep=";")
dataframe.columns = ["a","b","c","d","e","f","g","allLabels"]
dataframe = pd.concat([dataframe, deuxiemedata], ignore_index=True)
print(len(deuxiemedata))
# afficher la nouvelle dataframe combinée
print(len(dataframe))
# Diviser le DataFrame de manière aléatoire

# Diviser le DataFrame en deux parties
test =  pd.read_csv("ProjetDIA//finalTest.txt",sep=";")
test.columns = ["a","b","c","d","e","f","g"]
test.to_excel("ProjetDIA//resTest.xlsx")
test["allLabels"] = np.nan
#test  = test.assign(allLabels=np.nan)

# Afficher les deux sous-DataFrames
print("DataFrame 1:\n", dataframe)
print("\nDataFrame 2:\n", test)
#Calcul de la longeur à partir des valeurs d'initialisation
y_true = []
y_pred = []
for j in range(len(test)):
    commence = dt.datetime.now()
    distance = []
    for i in range(len(dataframe)):
            somme_carres = 0
            colonnes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
            for col in colonnes:
                somme_carres += (float(dataframe[col][i]) - float(test[col][j])) ** 2
                
            distance.append(math.sqrt(somme_carres))
    dataframe['Calcul'] = distance
    plusproche = sorted(distance)
    classdesneigbour = []
    for i in range(nneigborgh):
        ligneplusproche = dataframe[dataframe['Calcul'] == plusproche[i]]
        classdesneigbour.append(ligneplusproche['allLabels'].values[0])
    nombredevaleur = {element:classdesneigbour.count(element) for element in set(classdesneigbour)}
    print("Temps pris : "+str(dt.datetime.now()-commence))
    test["allLabels"][j] = max(nombredevaleur,key=nombredevaleur.get)
    #y_true.append(vraitest["allLabels"][j])
    #y_pred.append(test["allLabels"][j])
print("Fin calcul")
# Affichage de conclusion
#conf_matrix = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
#print(conf_matrix)

#report = classification_report(y_true, y_pred)
print("\nClassification Report:")
#print(report)

#dataframe.to_excel("Sortie1.xlsx")
test.to_excel("SortieFinal.xlsx")
df = test["allLabels"].astype(int)
df.to_csv("HenriSeranoTDI.txt",header=False,index=False)
print('La class de notre fleur la plus proche est ',str(ligneplusproche['allLabels'].values[0]))
