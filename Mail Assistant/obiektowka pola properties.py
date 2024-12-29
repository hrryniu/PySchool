class Poldek:
    def __init__(self, kolor):
        self.kolor = kolor
        self.ilosc_paliwa=10
        self.spalanie_na_100=12

    def zasieg(self):
        zasieg = self.ilosc_paliwa*100/self.spalanie_na_100
        return zasieg
    def hamuj(self):
        pass

poldek = Poldek('czerwony')
poldek.ilosc_paliwa +=10
poldek2= Poldek('zielony')

print(poldek.zasieg())
print(poldek2.zasieg())
#print(id(poldek.kolor)) #pola (zmienne)statyczne klasy są wspólne
#print(id(poldek2.kolor))
