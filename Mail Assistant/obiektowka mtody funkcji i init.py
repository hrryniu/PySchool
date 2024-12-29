class Polonez():
    def __init__(self):     #to SUPER metoda, której nie musimy wywołać. to inicjacyjna metoda gdy tworzymy obiekt; gdy nie nadamy żadnej metody to wywoła się metoda init
        print('polonez jest cool')
        self.hamuj()
    def hamuj(self):        #metoda funkcji
        print('oj joj hamuje oczami')
        self.skrecaj('lewo')

    def skrecaj(self,strona):        #wartosc domyslna strona=lewo, jesli nie podamy tego parametru
        print(f'skrecam w {strona}')
    def ilosc_paliwa(self):
        return '10 litrów'

    def info(self):
        print(self)

    def dodaj(self, a, b):
        return a + b



moj_polonez= Polonez()

#print(moj_polonez.dodaj(2,2))


#moj_polonez.hamuj()

#ilosc_paliwa = moj_polonez.ilosc_paliwa()
#print(ilosc_paliwa)
#moj_polonez.info()

#twoj_polonez = Polonez()
#twoj_polonez.info()