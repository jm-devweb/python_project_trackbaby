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
                dicData[i].append(lstLine[i])
            except :                                       # initialisation du premier élément de la liste
                dicData[i] = [lstLine[i]]                  # pour la 1 valeur, le type associé n'est pas connu       
    return dicData

###############################################################################"
# Fonction affichage d'un graphe
# param entrant : intGraph   : integer      : référence du graph
#                 dicData    : dinctionnary : dictionnaire des données comparatives
#                 dicMesure  : dinctionnary : dictionnaire des données comparatives
#                 intMesure  : integer      : indice dans le dictionnaire de mesure 
#                 strLab_y   : string       : libelle axe y
#                 strLab_leg : string       :  = libelle de la legende
#                 strLoc_leg : string       : = position de la legende
def graph(intGraph,dicData,dicMesure,intMesure,strLab_y,strLab_leg,strLoc_leg) :
    pyplot.subplot(1, 3, intGraph)                                   # Référence du graph pour la suite
    lstAxeX = [float(i) for i in dicData[0][1:]]                     # Récupération des données axe X
    for j in range(1,len(dicData)):                                  # Boucle sur index du dictionnaire
        pyplot.plot(
            lstAxeX,                                                 # liste contenant les données axe X                 
            [float(i) for i in dicData[j][1:]],                      # transformation en liste float d'un index
            label=dicData[j][0]+ " " + strLab_leg )                  # le libelle contenu dans [0] de la liste
    pyplot.legend( loc = strLoc_leg)
    pyplot.scatter([float(i) for i in dicMesure[0][1:]],[float(i) for i in dicMesure[intMesure][1:]])
    pyplot.xlabel('Age en mois') 
    pyplot.ylabel(strLab_y)
    pyplot.grid(True)

###############################################################################"
# Début
# 

# chargement des données light
dicWeights_boys  = load_file('poids-age-garcon-0-60-light.csv')
dicHeights_boys  = load_file('taille-age-garcon-0-60-light.csv')
dicSkulls_boys   = load_file('perim-cra-age-garcon-0-60-light.csv')
dicWeights_girls = load_file('poids-age-fille-0-60-light.csv')
dicHeights_girls = load_file('taille-age-fille-0-60-light.csv')
dicSkulls_girls  = load_file('perim-cra-age-fille-0-60-light.csv')

# chargement des données full
# dicWeights_boys  = load_file('poids-age-garcon-0-60.csv')
# dicHeights_boys  = load_file('taille-age-garcon-0-60.csv')
# dicSkulls_boys   = load_file('perim-cra-age-garcon-0-60.csv')
# dicWeights_girls = load_file('poids-age-fille-0-60.csv')
# dicHeights_girls = load_file('taille-age-fille-0-60.csv')
# dicSkulls_girls  = load_file('perim-cra-age-fille-0-60.csv')

# dictionnaire en fonction des genres
dicWeights = {'g': dicWeights_boys, 'f' : dicWeights_girls }
dicHeights = {'g': dicHeights_boys, 'f' : dicHeights_girls }
dicSkulls  = {'g': dicSkulls_boys , 'f' : dicSkulls_girls  }

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
graph(1,dicWeights[strGenre],dicMesure,1,'Poids en kg','poids','upper left')
graph(2,dicHeights[strGenre],dicMesure,2,'Taille en cm','taille','upper left')
graph(3,dicSkulls[strGenre],dicMesure,3,'Périmètre de la boite craniene en cm','périmètre cranien','lower right')
pyplot.show()