import getpass
opcje=["[papier" , "nozyce", "kamien"]
gracz1_wynik=0
gracz2_wynik=0
while gracz1_wynik != 3 or gracz2_wynik  != 3:
    wybor_gracza_jest_poprawny = True
    wybor_gracz1 = getpass.getpass("Gracz1 podaj swój wybór: ")
    if wybor_gracz1 in opcje:
        wybor_gracza_jest_poprawny = False
    wybor_gracz2 = input("Gracz2 podaj swój wybór: ")
    if wybor_gracz2 in opcje:
        wybor_gracza_jest_poprawny = False

    if wybor_gracz1 == "Papier" and wybor_gracz2 == "Kamień" or \
       wybor_gracz1 == "Nożyce" and wybor_gracz2 == "Papier" or \
       wybor_gracz1 == "Kamień" and wybor_gracz2 == "Nożyce":
        print("Gracz1 wygrał!")
        gracz1_wynik +=1
    elif wybor_gracz1 == wybor_gracz2:
        print("Remis")
    else:
        print("Gracz2 wygrał")
        gracz2_wynik +=1

if gracz1_wynik > gracz2_wynik:
    print("Wygrywa gracz1 !!!")
else:
    print("Wygrywa gracz2 !!!")