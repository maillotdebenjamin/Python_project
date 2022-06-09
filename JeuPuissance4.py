#!/usr/bin/python

def afficher_grille(grille):
    print("     0)  1)  2)  3)  4)  5)  6)")
    print("   ----------------------------")
    print("0)", end='')
    for i in range(7):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -----------------------------")
    print("1)", end='')
    for i in range(7):
        print(" | "+str(grille[i+7]), end='')
    print(" |")
    print("   -----------------------------")
    print("2)", end='')
    for i in range(7):
        print(" | "+str(grille[i+14]), end='')
    print(" |")
    print("   -----------------------------")
    print("3)", end='')
    for i in range(7):
        print(" | "+str(grille[i+21]), end='')
    print(" |")
    print("   -----------------------------")
    print("4)", end='')
    for i in range(7):
        print(" | "+str(grille[i+28]), end='')
    print(" |")
    print("   -----------------------------")
    print("5)", end='')
    for i in range(7):
        print(" | "+str(grille[i+35]), end='')
    print(" |")
    print("   -----------------------------")

def case_est_vide(grille,colonne,ligne):
    if ligne < 0:
        return True
    if grille[int(colonne)+int(ligne)*7]!=" ":
        return False
    else:
        return True

def est_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]==grille[3]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[2]) and (grille[1]==grille[3]) and (grille[1]==grille[4]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[3]) and (grille[2]==grille[4]) and (grille[2]==grille[5]) and (grille[2]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]==grille[6]) and (grille[3]!=" "):
        return 1
    
    if (grille[7]==grille[8]) and (grille[7]==grille[9]) and (grille[7]==grille[10]) and (grille[7]!=" "):
        return 1
    if (grille[8]==grille[9]) and (grille[8]==grille[10]) and (grille[8]==grille[11]) and (grille[8]!=" "):
        return 1
    if (grille[9]==grille[10]) and (grille[9]==grille[11]) and (grille[9]==grille[12]) and (grille[9]!=" "):
        return 1
    if (grille[10]==grille[11]) and (grille[10]==grille[12]) and (grille[10]==grille[13]) and (grille[10]!=" "):
        return 1
    
    if (grille[14]==grille[15]) and (grille[14]==grille[16]) and (grille[14]==grille[17]) and (grille[14]!=" "):
        return 1
    if (grille[15]==grille[16]) and (grille[15]==grille[17]) and (grille[15]==grille[18]) and (grille[15]!=" "):
        return 1
    if (grille[16]==grille[17]) and (grille[16]==grille[18]) and (grille[16]==grille[19]) and (grille[16]!=" "):
        return 1
    if (grille[17]==grille[18]) and (grille[17]==grille[19]) and (grille[17]==grille[20]) and (grille[17]!=" "):
        return 1
    
    if (grille[21]==grille[22]) and (grille[21]==grille[23]) and (grille[21]==grille[24]) and (grille[21]!=" "):
        return 1
    if (grille[22]==grille[23]) and (grille[22]==grille[24]) and (grille[22]==grille[25]) and (grille[22]!=" "):
        return 1
    if (grille[23]==grille[24]) and (grille[23]==grille[25]) and (grille[23]==grille[26]) and (grille[23]!=" "):
        return 1
    if (grille[24]==grille[25]) and (grille[24]==grille[26]) and (grille[24]==grille[27]) and (grille[24]!=" "):
        return 1
   
    if (grille[28]==grille[29]) and (grille[28]==grille[30]) and (grille[28]==grille[31]) and (grille[32]!=" "):
        return 1
    if (grille[29]==grille[30]) and (grille[29]==grille[31]) and (grille[29]==grille[32]) and (grille[29]!=" "):
        return 1
    if (grille[30]==grille[31]) and (grille[32]==grille[8]) and (grille[33]==grille[3]) and (grille[30]!=" "):
        return 1
    if (grille[31]==grille[32]) and (grille[31]==grille[33]) and (grille[31]==grille[34]) and (grille[31]!=" "):
        return 1
    
    if (grille[35]==grille[36]) and (grille[35]==grille[37]) and (grille[35]==grille[38]) and (grille[35]!=" "):
        return 1
    if (grille[36]==grille[37]) and (grille[36]==grille[38]) and (grille[36]==grille[39]) and (grille[36]!=" "):
        return 1
    if (grille[37]==grille[38]) and (grille[37]==grille[39]) and (grille[37]==grille[40]) and (grille[37]!=" "):
        return 1
    if (grille[38]==grille[39]) and (grille[38]==grille[40]) and (grille[38]==grille[41]) and (grille[38]!=" "):
        return 1
    
    if (grille[0]==grille[7]) and (grille[0]==grille[14]) and (grille[0]==grille[21]) and (grille[0]!=" "):
        return 1
    if (grille[7]==grille[14]) and (grille[7]==grille[21]) and (grille[7]==grille[28]) and (grille[7]!=" "):
        return 1
    if (grille[14]==grille[21]) and (grille[14]==grille[28]) and (grille[14]==grille[35]) and (grille[14]!=" "):
        return 1
    
    if (grille[1]==grille[8]) and (grille[1]==grille[15]) and (grille[1]==grille[22]) and (grille[1]!=" "):
        return 1
    if (grille[8]==grille[15]) and (grille[8]==grille[22]) and (grille[8]==grille[29]) and (grille[8]!=" "):
        return 1
    if (grille[15]==grille[22]) and (grille[15]==grille[29]) and (grille[15]==grille[36]) and (grille[15]!=" "):
        return 1
    
    if (grille[2]==grille[9]) and (grille[2]==grille[16]) and (grille[2]==grille[23]) and (grille[2]!=" "):
        return 1
    if (grille[9]==grille[16]) and (grille[9]==grille[23]) and (grille[9]==grille[30]) and (grille[9]!=" "):
        return 1
    if (grille[16]==grille[23]) and (grille[16]==grille[30]) and (grille[16]==grille[37]) and (grille[16]!=" "):
        return 1
    
    if (grille[3]==grille[10]) and (grille[3]==grille[17]) and (grille[3]==grille[24]) and (grille[3]!=" "):
        return 1
    if (grille[10]==grille[17]) and (grille[10]==grille[24]) and (grille[10]==grille[31]) and (grille[10]!=" "):
        return 1
    if (grille[17]==grille[24]) and (grille[17]==grille[31]) and (grille[17]==grille[38]) and (grille[17]!=" "):
        return 1
    
    if (grille[4]==grille[11]) and (grille[4]==grille[18]) and (grille[4]==grille[25]) and (grille[4]!=" "):
        return 1
    if (grille[11]==grille[18]) and (grille[11]==grille[25]) and (grille[11]==grille[32]) and (grille[11]!=" "):
        return 1
    if (grille[18]==grille[25]) and (grille[18]==grille[32]) and (grille[18]==grille[39]) and (grille[18]!=" "):
        return 1
   
    if (grille[5]==grille[12]) and (grille[5]==grille[19]) and (grille[5]==grille[26]) and (grille[5]!=" "):
        return 1
    if (grille[12]==grille[19]) and (grille[12]==grille[26]) and (grille[12]==grille[33]) and (grille[12]!=" "):
        return 1
    if (grille[19]==grille[26]) and (grille[19]==grille[33]) and (grille[19]==grille[40]) and (grille[19]!=" "):
        return 1

    if (grille[6]==grille[13]) and (grille[6]==grille[20]) and (grille[6]==grille[27]) and (grille[6]!=" "):
        return 1
    if (grille[13]==grille[20]) and (grille[13]==grille[27]) and (grille[13]==grille[34]) and (grille[13]!=" "):
        return 1
    if (grille[20]==grille[27]) and (grille[20]==grille[34]) and (grille[20]==grille[41]) and (grille[20]!=" "):
        return 1
    
    if (grille[14]==grille[22]) and (grille[14]==grille[30]) and (grille[14]==grille[38]) and (grille[14]!=" "):
        return 1
    if (grille[7]==grille[15]) and (grille[7]==grille[23]) and (grille[7]==grille[21]) and (grille[7]!=" "):
        return 1
    if (grille[15]==grille[23]) and (grille[15]==grille[31]) and (grille[15]==grille[39]) and (grille[15]!=" "):
        return 1
    
    if (grille[0]==grille[8]) and (grille[0]==grille[16]) and (grille[0]==grille[24]) and (grille[0]!=" "):
        return 1
    if (grille[8]==grille[16]) and (grille[8]==grille[24]) and (grille[8]==grille[32]) and (grille[8]!=" "):
        return 1
    if (grille[16]==grille[24]) and (grille[16]==grille[32]) and (grille[16]==grille[40]) and (grille[16]!=" "):
        return 1

    if (grille[1]==grille[9]) and (grille[1]==grille[17]) and (grille[1]==grille[25]) and (grille[1]!=" "):
        return 1
    if (grille[9]==grille[17]) and (grille[9]==grille[25]) and (grille[9]==grille[33]) and (grille[9]!=" "):
        return 1
    if (grille[17]==grille[25]) and (grille[17]==grille[33]) and (grille[17]==grille[41]) and (grille[17]!=" "):
        return 1

    if (grille[2]==grille[10]) and (grille[2]==grille[18]) and (grille[2]==grille[26]) and (grille[2]!=" "):
        return 1
    if (grille[10]==grille[18]) and (grille[10]==grille[26]) and (grille[10]==grille[34]) and (grille[10]!=" "):
        return 1
    if (grille[3]==grille[11]) and (grille[3]==grille[19]) and (grille[3]==grille[27]) and (grille[3]!=" "):
        return 1

def recup_coord(colonne):
    while (1):
        colonne = input("Entrez le numero de la colonne : ")
        try:
            colonne = int(colonne)
            if (colonne > 6 or colonne < 0):
                print("please enter a good number")
                continue
            return (colonne)
        except:
            print("please enter a good number")
            continue

def tour(grille, joueur, ligne = 5):
    colonne = ""
    print("C'est le tour du joueur "+str(joueur))
    colonne = recup_coord(colonne)
    print(f"Vous avez joué la case {colonne}")
    if grille[int(colonne)+int(ligne)*7] != " ":
        while not case_est_vide(grille,colonne,ligne):
            ligne -= 1
        if ligne == -1:
            print("plus de place dans cette colonne")
            tour(grille, joueur, 5)
    if joueur==1 :

        grille[int(colonne)+int(ligne)*7]="X"
    if joueur==2 :

        grille[int(colonne)+int(ligne)*7]="O"
    afficher_grille(grille)



joueur=1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
grille=[" " for i in range(42)]
print(afficher_grille(grille))
gagne = 0
while gagne == 0:
    tour(grille, joueur)
    if est_gagnant(grille):
        print("Le joueur "+str(joueur)+" remporte la partie")
        gagne=1
    # changement de joueur
    if joueur==1:
        joueur=2
    else:
        joueur=1