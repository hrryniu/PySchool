gracz1_wynik=0
gracz2_wynik=0
opcje=["papier", "nozyce", "kamien"]
def pobierz_wybor(gracz):
  while True:
        wybor_gracza = input(f"{gracz} podaj swój wybór: ")
        if wybor_gracza in opcje:
            return wybor_gracza

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == wybor_gracza2:
        print("remis")
        return 0

    wynik = {
        ('papier','kamien'):1,
        ('kamien','nozyce'):1,
        ('nozyce', 'papier'):1
    }
    return wynik.get((wybor_gracza1,wybor_gracza2), -1)

while gracz1_wynik != 3 and gracz2_wynik  != 3:
    wybor_gracza1 = pobierz_wybor('Gracz1')
    wybor_gracza2 = pobierz_wybor('Gracz2')
    wynik = sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik ==1:
        print("Gracz 1 wygrał tę rundę")
        gracz1_wynik +=1

    elif wynik == -1:
        print("Gracz 2 wygrał tę rundę")
        gracz2_wynik +=1


if gracz1_wynik > gracz2_wynik:
    print("Wygrywa gracz1 !!!")
else:
    print("Wygrywa gracz2 !!!")