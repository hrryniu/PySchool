while True:
    try:
        x = int(input("What's x? "))
    except ValueError:  #poradzenie sobie z błedem
        print("x is not an integer")
    else:           #jeśli program nie wejdzie w sekcję "except"
       break

 print(f"x is {x}")