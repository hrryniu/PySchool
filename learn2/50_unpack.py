def total(galleons, sickles, knuts):
    return (galleons*17+sickles)*29+knuts


# prostacki sposób
#print(total(100,50,25), "Knuts")

#---------
#sopsob podatny na błędy
# coins=[100,50,25]
# print(total(coins[0],coins[1],coins[2]), "Knuts")

#-----metoda unpadking, rozkowuje poszczególne elementy listy
coins=[100,50,25]
print(total(*coins), "Knuts")

#można też rozpakować słownik/distionary/ ale to tego potrzeba wpisać nie jedną ale dwie gwiazdki

#jeśli w liście pojawi się jakiś nowy argument to rozpakowanie się
# nie uda bo funkcja total potrzebuje tylko trzech argumentów
#ROZWIĄZANIE W PLIKU 51