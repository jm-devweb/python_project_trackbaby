##### Programme n°1

# Import
import nourrisson

# Tableaux des données
low_weights = {'g':nourrisson.low_weights_boys,'f': nourrisson.low_weights_girls}
high_weights = {'g':nourrisson.high_weights_boys,'f': nourrisson.high_weights_girls}
low_heights = {'g':nourrisson.low_heights_boys,'f': nourrisson.low_heights_girls}
high_heights = {'g':nourrisson.high_heights_boys,'f': nourrisson.high_heights_girls}
low_skulls = {'g':nourrisson.low_skulls_boys,'f': nourrisson.low_skulls_girls}
high_skulls = {'g':nourrisson.high_skulls_boys,'f': nourrisson.high_skulls_girls}

# Genre
libelle= {'g':'un garcon','f':'une fille'}

###############################################################################"
# Début
# 
print ("Bienvenue dans ce programme de vérification des constantes de votre nourrisson !")

# Genre : Saisie / Vérification g ou f 
strGenre = ''
while True:
    strGenre = str(input ("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille), ctr-d pour quitter : "))
    strGenre = strGenre.lower()  # minuscule
    if  strGenre == 'g' or strGenre == 'f' : 
        break

# Age : Saisie / Vérification bornes entre 0 et 60 en entier
strAge = ''
while True:
    strAge = input ("Veuillez entrez l'age de votre nourrisson (entre 0 et 60 mois), ctr-d pour quitter : ")
    try : 
        intAge = int(strAge)
        if  (intAge >= 0 and intAge <= 60) :
            break
    except :
        print("Erreur lors de la conversion de l'age : ",strAge )
   
# Poids : Saisie / Vérification suppérieur à 0
strPoids = ''
while True:
    strPoids = input ("Veuillez entrez le poids de votre nourrisson en kg, ctr-d pour quitter : ")    
    try : 
        fltPoids = float(strPoids)
        if  fltPoids > 0 :
            break
    except :
        print("Erreur lors de la conversion du poids : ", strPoids )

# Taille : Saisie / Vérification suppérieur à 0
strTaille = ''
while True:
    strTaille = input ("Veuillez entrez la taille de votre nourrisson en cm, ctr-d pour quitter : ")   
    try : 
        fltTaille = float(strTaille)
        if  fltTaille > 0  :
            break
    except :
        print("Erreur lors de la conversion de la taille : ", strTaille)

# Périmetre : Saisie / Vérification suppérieur à 0
strPerimetre = ''
while True:
    strPerimetre =input ("Veuillez entrez le périmetre cranien de votre nourrisson en cm, ctr-d pour quitter : ")    
    try : 
        fltPerimetre = float(strPerimetre)
        if  fltPerimetre > 0 :
            break
    except :
        print("Erreur lors de la conversion du périmètre : ", strPerimetre)

# Check poids
print()
print("La norme de poids pour " + libelle[strGenre] + " de "  + str(intAge) + " mois est situé ente " + str(low_weights[strGenre][intAge]) + " kg et " 
+ str(high_weights[strGenre][intAge])  + " kg ")    
if low_weights[strGenre][intAge] < fltPoids and high_weights[strGenre][intAge] > fltPoids : 
    print("Le poids de votre nourrison ("+str(fltPoids)+" kg) est dans la norme !")
else:    
    print("Le poids de votre nourrison ("+str(fltPoids)+" kg) n'est pas dans la norme !")

# Check Taille
print()
print("La norme de taille pour " + libelle[strGenre] + " de "  + str(intAge) + " mois est situé ente " + str(low_heights[strGenre][intAge]) + " cm et " 
+ str(high_heights[strGenre][intAge])  + " cm ")    
if low_heights[strGenre][intAge] < fltTaille and high_heights[strGenre][intAge] > fltTaille : 
    print("La taille de votre nourrison ("+str(fltTaille)+" cm) est dans la norme !")
else:    
    print("La taille de votre nourrison ("+str(fltTaille)+" cm) n'est pas dans la norme !")

# Check perimetre
print()
print("La norme de périmetre cranien pour " + libelle[strGenre] + " de "  + str(intAge) + " mois est situé ente " + str(low_skulls[strGenre][intAge]) + " cm et " 
+ str(high_skulls[strGenre][intAge])  + " cm ")    
if low_skulls[strGenre][intAge] < fltPerimetre and high_skulls[strGenre][intAge] > fltPerimetre : 
    print("Le périmetre cranien de votre nourrison ("+str(fltPerimetre)+" cm) est dans la norme !")
else:    
    print("Le périmetre cranien de votre nourrison ("+str(fltPerimetre)+" cm) n'est pas dans la norme !")