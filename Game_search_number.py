#!/usr/bin/python

from random import randint
A = randint(0 , 100)
print(A)
nombre = 0
while nombre != A:
    nombre = int(input( "entrer un nombre "))
    if nombre > A:
        print(" plus petit")
    else:
        print("plus grand ")
if nombre == A :
    print( "Bravo")