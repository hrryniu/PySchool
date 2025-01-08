#inheritance rozumiem jako dziedziczenie. żeby nie potwarzać atrybutów klas, możemy zrobić jadną klasę wspólną
# np. wizard, możemy nadać tej klasie atrybut- imię. i potem możemy zrobić dziedziczne
#klasy student, i profesor, które będą dziedziczyły atrybut imienia

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house= house

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject= subject