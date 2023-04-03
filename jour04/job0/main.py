def factorielle(x):
    if x == 1:
        return 1
    else:
        return (x * factorielle(x-1))

x = input("Renseigne moi un nombre entier : ")
y = factorielle(int(x))
print(f"la factorielle de {x} est : {y}")
    