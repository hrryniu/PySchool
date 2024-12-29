#kompozycja mowi ze obiekt cos ma
#dziedziczenie mowi ze obiekt jest jakiś

class Auto:
    def __init__(self, silnik): -> None:
        self.silnik = silnik


class Silnik:
    def __init__(self, pojemnosc) -> None:
        self.pojemnosc=pojemnosc

silnik=Silnik(5000)
asam_auto=Auto(silnik)

print(adam_auto.silnik.pojemnosc)

adam_auto=Auto(5000)