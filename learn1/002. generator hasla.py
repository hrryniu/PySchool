import sys
import random
import string
password= []
characters_left = -1

def update_characters_left(numbers_of_characters):
    global characters_left
    if numbers_of_characters > characters_left or numbers_of_characters < 0:
            print("Liczba znaków spoza przedziału 1-", numbers_of_characters)
            sys.exit(0)
    else:
        characters_left -= numbers_of_characters #tutaj  nie wiem czy bedzie ok
        print("Pozostało znaków: ", characters_left)

password_length= int(input(" Jak długie ma być hasło? "))

if password_length < 5:
    print("Hasło musi mieć minimum 5 znaków, spróbuj jeszczw raz")
    sys.exit(0)
else:
    characters_left = password_length


lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))

update_characters_left(lowercase_letters)
uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))

update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))

update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))

update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane, hasło zostanie uzupełnione małymi znakami")
    lowercase_letters += characters_left

print()
print("Długość hasła: ", password_length)
print("Małe litery: ", lowercase_letters)
print("Duże litery: ", uppercase_letters)
print("Znaki specjalne: ", special_characters)
print("Cyfry: ", digits)

for i in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło: ", "".join(password))