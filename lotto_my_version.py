from random import randint

def lotto():
    lista =[]

    while True:
        try:
            my_choice1 = int(input("Wprowadź cyfrę od 1 - 49: "))
            if my_choice1 <1 or my_choice1 > 49:
                print("Możesz wybrać tylko cyfry 1-49")
            else:
                lista.append(my_choice1)
                break
        except ValueError:
            print("To nie liczba!")

    while True:
        try:
            my_choice2 = int(input("Wprowadź cyfrę od 1 - 49: "))
            if my_choice2 in lista:
                print("Ta liczba już została wybrana! Wybierz inną")
            elif my_choice2 > 49 or my_choice2 <1:
                print("Możesz wybrać tylko cyfry 1-49")
            else:
                lista.append(my_choice2)
                break
        except ValueError:
            print("To nie liczba!")

    while True:
        try:
            my_choice3 = int(input("Wprowadź cyfrę od 1 -49: "))
            if my_choice3 in lista:
                print("Ta liczba już została wybrana!")
            elif my_choice3 > 49 or my_choice3 <1:
                print("Możesz wybrać tylko cyfry 1-49")
            else:
                lista.append(my_choice3)
                break
        except ValueError:
            print("To nie liczba!")

    while True:
        try:
            my_choice4 = int(input("Wprowadź cyfrę od 1 - 49: "))
            if my_choice4 in lista:
                print("Ta liczba już została wybrana!")
            elif my_choice4 > 49 or my_choice4 <1:
                print("Możesz wybrać tylko cyfry 1-49")
            else:
                lista.append(my_choice4)
                break
        except ValueError:
            print("To nie liczba!")

    while True:
        try:
            my_choice5 = int(input("Wprowadź cyfrę od 1 -49: "))
            if my_choice5 in lista:
                print("Ta liczba już została wybrana!")
            elif my_choice5 > 49 or my_choice5 <1:
                print("Możesz wybrać tylko cyfry 1- 49")
            else:
                lista.append(my_choice5)
                break
        except ValueError:
            print("To nie liczba!")

    while True:
        try:
            my_choice6 = int(input("Wprowadź cyfrę od 1 - 49: "))
            if my_choice6 in lista:
                print("Ta liczba już została wybrana!")
            elif my_choice6 > 49 or my_choice6 <1:
                print("Możesz wybrać tylko cyfry 1-49")
            else:
                lista.append(my_choice6)
                break
        except ValueError:
            print("To nie liczba!")

    lista = sorted(lista)
    print("Twoje numery: ",lista)

    lucky_numbers = []
    for n in range(1,7):
        rnd = randint(1,50)
        while rnd in lucky_numbers:
            rnd = randint(1, 50)

        lucky_numbers.append(rnd)
    lucky_numbers = sorted(lucky_numbers)
    print("Wylosowane liczby: ", lucky_numbers)



    covered_numbers =[]
    for i, j in zip(lista, lucky_numbers):
        if i == j:
            covered_numbers.append(i)

    score = len(covered_numbers)

    if score == 6:
        print("BRAWOOOOOOOOOOO!")
    elif score == 5:
        print("Było tak blisko!!!")
    elif score == 4:
        print("Wygrałeś czwórkę!")
    elif score == 3:
        print("Wygrałeś trójkę!")
    else:
        print("Buuuu!Nic nie wygrałeś!")


lotto()







