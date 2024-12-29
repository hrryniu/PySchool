gracz1_wynik=0
gracz2_wynik=0
opcje=["[papier" , "nozyce", "kamien"]
def pobierz_wybor(gracz):
  while True:
        wybor_gracza = input(f"{gracz} podaj swój wybór: ")
        if wybor_gracza1 in opcje:
            return wybor_gracza

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == "Papier" and wybor_gracza2 == "Kamień" or \
       wybor_gracza1 == "Nożyce" and wybor_gracza2 == "Papier" or \
       wybor_gracza1 == "Kamień" and wybor_gracza2 == "Nożyce":
        print("Gracz1 wygrał!")
        return 1
    elif wybor_gracza1 == wybor_gracza2:
        print("Remis")
        return 0
    else:
        print("Gracz2 wygrał")
        return -1

while gracz1_wynik != 3 or gracz2_wynik  != 3:
    wybor_gracza1 = pobierz_wybor('Gracz1')
    wybor_gracza2 = pobierz_wybor('Gracz2')
    wynik = sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik ==1:
        gracz1_wynik +=1
    elif wynik == -1:
        gracz2_wynik

if gracz1_wynik > gracz2_wynik:
    print("Wygrywa gracz1 !!!")
else:
    print("Wygrywa gracz2 !!!")