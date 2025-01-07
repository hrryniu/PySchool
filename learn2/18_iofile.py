names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True): #posortowanie wyświetlania plików, parametr reverse odpowiada za wyswietlanie od tyłu
    print(f"hello, {name}")
#for _ in range(3): #pętla która pobierze od użytkowanika 3 razy imię i zappenduje je do listy names
 #   name = input("What's your name? ")
 #   names.append(name)

#for name in sorted(names): #wypisanie imion w koleności alfabetycznej .sorted
 #   print(f"hello, {name}")

#-----------
# name=input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
#
# with open("names.txt" , "r") as file:
#     for line in lines:
#         print("Hello", line, end="")
#----------------------

#podejscie bardziej rozpisane ale nie najlepsze
# name=input("What's your name? ")
# file= open("names.txt", "a")  #otwieramy plik w trybie write(nadpisuje cały plik)
# file.write(f"{name}\n")
# file.close()