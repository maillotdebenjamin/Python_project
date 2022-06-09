#!/usr/bin/python

def affiche (mot , nomb = 0 , Compt = 0 , lettre = "i" , tableau = []):
    A = []
    compt = 0
    for i in mot:
        A.append(i)
    if nomb == 0:
        return tableau
    if nomb != 0:
        for j in A:
            compt += 1
            if lettre == j:
                tableau[compt-1] = lettre
                print(tableau)


def pendu(le_mot, play , reussie = 0):
    B = ["_" for j in le_mot]
    C = [0 for i in le_mot]
    while play > 0:
        print(affiche(le_mot, 0 , 0 , "" , B))
        mot_demander = input( " entrer une lettre:")
        if len(mot_demander) > 1:
            print(" please enter letter")
            continue
        gagner = 0
        aide = len(le_mot) - 1
        #print(aide)
        compt = 0
        for i in le_mot:
            compt = compt + 1
            #print(i)
            aide = aide -1
            if i == mot_demander:
                print("bien ")
                affiche(le_mot, 1 , compt-1 , i , B)
                aide += 10
                gagner += 1
                if C[compt-1] == 0:
                    C[compt-1] = 1
            if aide < 0:
                play = play - 1
                print(f"il vous reste {play} tentative")
        for x in C:
            if x == 1:
                gagner += 1
        if gagner == len(le_mot)+1:
            return "Bravo tu as trouvé"
    else :
        return "vous avez perdu "

print(pendu("rien", 10 ))