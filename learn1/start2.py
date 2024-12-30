light =input("Jakie widzisz światło? \n")

match light:
    case 'zielone':
        print("Możesz jechać")
    case 'czerwone':
        print("stój")

i=1
while i<5:
    print(i)
    i+=1

name = None
while name!= "Kamil":
    name= input("Jak masz na imię?: ")

print("OOOOO, cześć typie!")