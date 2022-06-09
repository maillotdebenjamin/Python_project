#!/usr/bin/python

from random import randint
A = randint(0 , 100)

nombre = 0
print("enter 'q' to quit")
while nombre != A:
    nombre = input( "entrer un nombre :")
    try:
        nombre = int(nombre)
    except:
        print(nombre)
        if (nombre == "q"):
            break
        print("bad number")
        continue
    if nombre > A:
        print(" plus petit")
    else:
        print("plus grand ")
if nombre == A :
    print( "Bravo")