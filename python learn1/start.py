# imie = input("Jak masz na imie?\n")
# nazwisko = input("Jakie masz nazwisko?\n")
# wiek = input("Ile masz lat?\n" )
#
# print("Imie: " + imie + "\n" + "Nazwisko: " + nazwisko + "\n" + "Wiek: " + wiek)

a=2
b=7
#działania matematyczne
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
#operatory porównawcze
print(a == b)
print(a > b)
print(a >=b)
print(a < b)
print(a != b)
#operatory logiczne
print(a > b and b > 0)
print(a < b and b > 3)
print(a > 10 or (b > 0 and a < b))


a+= 1
print(a)

channel_name= "Jimbo Media"

print(channel_name.upper) #wypisuje string z wielkich liter
print(channel_name.lower())  #wypisuje string z małych liter
print(channel_name)

napis = "    sssss      "
print(napis.strip) #pozbawia białych znaków(spacji) na początku i na końcu
print(napis.upper().startswith("o"))  #możemy łaczyć metody
napis2 = "nananana"
print(napis2.capitalize()) #zaczyna string od duzej litery
print(napis2.startswith("O"))
#print(channel_name.replace( __old:"Jimbo", __new:"Hryniu")) #zamiana
print(channel_name.split(" "))

#slicing
print(channel_name[0:4])

#instrukcje warunkowe

light = input("Jakie jest światło?: Zielone, czerwone, żółte, inne?: \n")

if light =="zielone":
    print("można jechać")
elif light == "żółte":
    print("przygotuj się")
elif light =="czerwone":
    print("stój")