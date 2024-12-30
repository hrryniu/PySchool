students = [ #tworzę listę
    {"name" : "Hermione" , "house": "Gryffindor" , "patronus" : "Otter"},
    {"name" : "Harry" , "house": "Gryffindor" , "patronus" : "Stag"},
    {"name" : "Ron" , "house": "Gryffindor" , "patronus" : "Jack Russell terrier"},
    {"name" : "Draco" , "house": "Slytherin" , "patronus" : "None"},
]


#zwijany nawias to słownik

#wypisywanie wartosći dla kluczy w pętki
for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")