def sorted_integer():
    iteration = 0
    numbers = []
    while(len(numbers) < 5):
        number = int(input("Entrez un nombre entier : "))
        numbers.append(number)

    numbers.sort()
    print(numbers)

sorted_integer()