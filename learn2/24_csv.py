import csv
students =[]

with open("students.csv") as file:
    reader= csv.DictReader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

    #for line in file:
      #  name, house = line.rstrip().split(",")
        #students.append(f"{name} is in {house}")

        # print(f"{name} is in {house}")
      #  student = {"name": name, "house":house}
      #  students.append(student)

#def get_name(student):
#    return student["name"]

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}")
