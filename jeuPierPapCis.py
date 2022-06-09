#!/usr/bin/python

from random import randint
def Jeux():
    A = ["ciseaux","papier","pière"]
    play = True
    tour = 0
    while play == 0:
        print("0-ciseaux , 1-papier , 2-pière")
        try:
            reponse = int(input("entrer une reponse:"))
        except:
            print("bad entry")
            continue
        if tour == 0:
            choix = randint(0,2)
            print(A[choix])
            tour += 1
        if reponse == choix:
            print("égalité")
            Jeux()
        if reponse == 0 and choix == 1:
            print("tu as gagné")
            play+=1
        if reponse == 1 and choix == 2:
            print("tu as gagné")
            play+=1
        if reponse == 2 and choix == 0:
            print("tu as gagné")
            play+=1
        if reponse == 1 and choix == 0:
            print("perdu")
            play+=1
        if reponse == 2 and choix == 1:
            print("perdu")
            play+=1
        if reponse == 0 and choix == 2:
            print("perdu")
            play+=1




Jeux()