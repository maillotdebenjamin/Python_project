#!/usr/bin/python

gril=[" " for i in range(100)]
def afficher_grille(grille):
    print("     0)  1)  2)  3)  4)  5)  6)  7)  8)  9)")
    print("   ----------------------------------------")
    print("0)", end='')
    for i in range(10):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("1)", end='')
    for i in range(10):
        print(" | "+str(grille[i+10]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("2)", end='')
    for i in range(10):
        print(" | "+str(grille[i+20]), end='')
    print(" |")
    print("   -----------------------------------------")
    print("3)", end='')
    for i in range(10):
        print(" | "+str(grille[i+30]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("4)", end='')
    for i in range(10):
        print(" | "+str(grille[i+40]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("5)", end='')
    for i in range(10):
        print(" | "+str(grille[i+50]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("6)", end='')
    for i in range(10):
        print(" | "+str(grille[i+60]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("7)", end='')
    for i in range(10):
        print(" | "+str(grille[i+70]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("8)", end='')
    for i in range(10):
        print(" | "+str(grille[i+80]), end='')
    print(" |")
    print("   ----------------------------------------")
    print("9)", end='')
    for i in range(10):
        print(" | "+str(grille[i+90]), end='')
    print(" |")

print(afficher_grille(gril))