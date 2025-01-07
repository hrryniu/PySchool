import re
email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|eu|pl)$", email, re.IGNORECASE): #IGNORECASE sprawia ze nie bieżemy pod uwagę rozmiaru znaków
    print("Valid")
else:
    print("Invalid")
    #
    # (\w+\.)?  <= opcjonalnie możemy dodać ciąg znaków zakończonych kropką- czyli możemy dodać subdomenę do adresu
    # \w oznacza kazdy znak alfabetyczny i numeryczny => (r"^\w+@\w+\.edu$")
    #   (r"^[^@]+@[^@]+\.edu$") - jeden ze sposobów
    # . oznacza dowolny znak poza nową linią
    # * oznacza 0 lub więcej powtorzen
    # + oznacza 1 lub wiecej powtorzeń
    # r oznacza tryb formatowania RAW string, dzięki temu backslash nie jest interpretowany jako wyjście do nowej linii
    # \(backslash) oznacza że chcemy w trybie walidacji  zobaczyc kropkę. normalnie
    # kropka oznacza że chcemy zobaczyć w jej miejscu dowolny znak, ale gdy chcemy aby w validowanym
    # ciągu, pojawiła się kropka a nie dowolny znak to trzeba przed nią wstawić \
    #zatem jesli chcemy żeby input był valid to musimy użyć \.edu
    # ^ na początku i $ na końcu pokazuje dokładnie gdzie jest początek i koniec inputu uzytkownika
    # [^@] - oznacza ze przyjmujie każdy symbol poza @