#w dziedziczeniu syn dziedziczy wszystko po tacie, potrafi wszystko co on i ma wszystko to co tata
#POLONEZ  jest POJAZDEM SPALINOWM , które jest AUTEM

#zacznijmy od góry(auto)

class Auto:
    def __init__(self,waga):
        self.waga =waga
        print("ADAMO")

    def jedz(self):
        print('jade')

class AutoSpalinowe(Auto):
    def __init__(self, ilosc_cylindrow,waga):
        print('Wow Wow')
        self.ilosc_cylindrow = ilosc_cylindrow
        super().__init__(waga)

    def sprawdz_olej(self):
        return 'olej jest ok'

class Polonez(AutoSpalinowe):
    def __init__(self,model,ilosc_cylindrow,waga):
        self.model =model
        super().__init__(ilosc_cylindrow, waga)

    def jazda_bokiem(self):
        print('jade bokiem')



auto_spalinowe = Polonez('caro plus',6,1450)
print(auto_spalinowe.waga)