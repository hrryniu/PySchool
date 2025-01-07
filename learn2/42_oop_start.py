def main():
    student= get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name= input("Name: ")
    house= input("House: ")
    return (name, house) #to raczej domen pythona żeby zwracać więcej niż jedną wartość.
                        #a tak naprawdę zwracamy jedną wartość, którą jest tuple z dwoma elementami
            # gdyby wartości returna były w twardym nawiasie [] to zwróciłby nie tuple ale listę 

if __name__ == "__main__":
    main()


