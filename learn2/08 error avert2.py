def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

main()

#w tej wersji zastosowałem argument dla funkcji get_int a w
#definicji funkcji get_int użyłem zwrotu: prompt