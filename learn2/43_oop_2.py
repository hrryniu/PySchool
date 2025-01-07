def main():
    student= get_student()
    print(f"{student['name']} from {student['house']}")

#napisane nieco bardziej amatorsko
# def get_student():
#     student={}
#     student["name"]= input("Name: ")
#     student["house"]= input("House: ")
#     return student

#napisane lepiej:
def get_student():
    name= input("Name: ")
    house= input("House: ")
    return {"name": name, "house":house}
if __name__ == "__main__":
    main()


