import json     #pracuje z json więc potrzebujemy biblioteki
points= 0  #tworzę od razu zmienną do liczenia punktów, na początku mam ich zero

def show_question(question):
    global points #dajemy funkcji dostęp do zmiennej points
    print()
    print(question["pytanie"])
    print("a",question["a"])
    print("b", question["b"])
    print("c", question["c"])
    print("d", question["d"])
    print()

    answer= input("Którą odpowiedź wybierasz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("Prawidłowa odpowiedź. Masz", points, "punktów")
    else:
        print("Zła odpowiedź")

with open("quiz.json") as json_file: #importuję plik jako zmienną json_file
   questions= json.load(json_file)  #odczytuję plik do zmiennej questions

   for i in range(0,len(questions)):
       show_question(questions[i])

print()
print("To koniec gry, zdobyte punkty:",points,".")
#print("To koniec gry, zdobyte punkty:"+str(points)+".")  #przy łączeniu zmiennych z tekstem w princie poprzez "+" to trzeba zamienić zmienną na string