import csv

name= input("What's your name? ")
home= input("Where's Your home? ")

with open("Students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])