##### Programme n°2

# On importe les modules qui vont nous permettre de traiter les données

# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as pyplot
# csv pour lire les fichiers de données
import csv

###############################################################################"
# Fonction de chargement des donnnées
# Description : Charge un fichier au format suivant :
#               - la premiére ligne est la ligne d'entete
#               - la première colonne correspond aux données de l'axe x
# param entrant : file : string : Nom du fichier à charger
# param sortant : dictionnaire contenant les données
#                 - clé : 0 à n-1, n étant le nb de colonne dans le fichier
#                 - donnée associée : liste contenant les données en colonnne
#                                     le premier élément de la liste contient l'entête de colonne    
def load_file(fSource) :
    dicData = {}                                           # Dictionnaire renvoyé
    for strLine in open(fSource,"r").readlines():          # Boucle sur les lignes du fichier   
        lstLine = strLine.rstrip('\n').split(';')
        for i in range(0,len(lstLine)) :                   # Boucle sur les colonnes du fichier
            try :    
                dicData[i].append(float(lstLine[i]))
            except :                                       # initialisation du premier élément de la liste
                dicData[i] = [lstLine[i]]                  # pour la 1 valeur, le type associé n'est pas connu       
    return dicData

###############################################################################"
# Fonction affichage d'un graphe
# param entrant : intGraph   : integer      : référence du graph
#                 dicData    : dinctionnary : dictionnaire des données comparatives
#                 dicMesure  : dinctionnary : dictionnaire des données comparatives
#                 strLab_y   : string       : libelle axe y
#                 strLab_leg : string       : libelle de la legende
#                 strLoc_leg : string       : position de la legende
def graph(intGraph,dicData,dicMesure,strLab_y,strLab_leg,strLoc_leg) :
    pyplot.subplot(1, 3, intGraph)                                   # Référence du graph pour la suite
    [pyplot.plot(dicData[0][1:],dicData[i][1:],label=dicData[i][0]+ " " + strLab_leg ) for i in range(1,len(dicData))]
    pyplot.legend( loc = strLoc_leg)
    pyplot.scatter(dicMesure[0][1:],dicMesure[intGraph][1:])
    pyplot.xlabel('Age en mois') 
    pyplot.ylabel(strLab_y)
    pyplot.grid(True)

###############################################################################"
# Début
# 

# chargement des données light
# Dictionnaire des normes
# Niveau 1 :
#   Clé  : Type (poids,taille)
#   Data : 
#          Liste :
#                   1 : Numéro du graph
#                   2 : Dictionnaire
#                             Clé   :  Genre 
#                              Data :  Contenu du fichier
#                   3 : Libelle  Y
#                   4 : libelle  legende
#                   5 : position legende   
dicNorme ={'W':[1,{'g':load_file('poids-age-garcon-0-60-light.csv'),'f':load_file('poids-age-fille-0-60-light.csv')},'Poids en kg','poids','upper left'],'T':[2,{'g': load_file('taille-age-garcon-0-60-light.csv'),'f':load_file('taille-age-fille-0-60-light.csv')},'Taille en cm','taille','upper left'],'S':[3,{'g': load_file('perim-cra-age-garcon-0-60-light.csv'),'f':load_file('perim-cra-age-fille-0-60-light.csv') },'Périmètre en cm','périmètre','lower right']}      

# chargement des mesures
dicMesure = load_file('mesures.csv')

# Genre : Saisie / Vérification g ou f 
strGenre = ''
while True:
    strGenre = str(input ("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille), ctr-d pour quitter : "))
    strGenre = strGenre.lower()  # minuscule
    if  strGenre == 'g' or strGenre == 'f' : 
        break

# Affichage du graph
[graph(dicNorme[Mykey][0],dicNorme[Mykey][1][strGenre],dicMesure,dicNorme[Mykey][2],dicNorme[Mykey][3],dicNorme[Mykey][4]) for Mykey in dicNorme.keys()]
pyplot.show()