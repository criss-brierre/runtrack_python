import random

def puissance(x,n):
    if n == 0:
        return 1
    return x*puissance(x,n-1)

x = input("Donnez nous une valeur :")
n = input("Donnez nous la puissance que voulez : ")

print(f"{x} puissance de {n} = {puissance(int(x),int(n))}")
