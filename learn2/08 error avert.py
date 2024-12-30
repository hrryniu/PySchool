#wersja dłuższa ale czytelniejsza
#w tym programie użyłem po raz pierwszy try, except, i pass
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            #print("x is not an integer") informacja dla użytkownika
            pass #taka komenda w przypadku nie wpisania int po prostu powtarza zapytanie
        else:
            break
    return x

main()


#wersja krótsza ale mniej zrozumiała dla początkującego

# def main():
#     x = get_int()
#     print(f"x is {x}")
#
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#
# main()