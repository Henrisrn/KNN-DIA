import pandas as pd

#bii = pd.read_excel("SortieFinal.xlsx")
#bii.to_csv("HenriSeranoTDI.txt", index=False, header=False)
data = pd.read_csv("HenriSeranoTDI.txt", header=None)
print(data)
data.columns = ["allLabels"]
# Nettoyage des données dans data
#data = bii
databis = pd.read_csv("C://Users//henri//Downloads//Final_resultKNN.txt", header=None, encoding='latin1')
databis.columns = ["labels"]
print(databis)
# Nettoyage des données dans databis
databis['labels'] = databis['labels'].apply(lambda x: str(x).strip())

compteur = 0
for i in range(len(data["allLabels"])):
    if str(data["allLabels"][i]) != str(databis["labels"][i]):
        compteur += 1
        print("différents ce que j'ai : ", data["allLabels"][i], " ce qu'il a ", databis["labels"][i], " à l'index ", i)

print("Nombre de valeurs différentes : ", compteur)
