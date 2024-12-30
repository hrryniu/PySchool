import sys
no_of_tries = 5
word = 'Kamil'
used_letters = []

user_word=[] #tworzymy listę gdzie będziemy zapisywać litery podane przez uzytkownika

def find_indexes(word,letter):
    indexes=[]

    for index, letter_in_word in enumerate(word):
        if letter==letter_in_word:
            index.append(index)

    print(enumerate(word))

    return indexes
for _ in word:
    user_word.append("_")
while True:  #to jest pętla nieskonczona
    letter = input("Podaj litere: ")
    used_letters.append(letter)

    found_indexes=find_indexes(word, letter)
    if len(found_indexes)==0:
        print("Nie ma takiej litery!")]
        no_of_tries-=1
        print("Pozostało prób: " + no_of_tries)
        if no_of_tries==0:
            print("Koniec gry!")
            sys.exit(0)

    print("Użyte liter: " +used_letters)