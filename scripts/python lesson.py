#!/bin/python3

import sys #import system functions and parameters
from datetime import datetime as dt

def new_line():
    print('\n')

new_line()

#Advanced Strings
print("Advanced settings")
my_name='Mat'
print(my_name[0]) #first initial
print(my_name[-1]) #last initial

sentence = "This is sentence."

print(sentence[:4]) #first word
print(sentence[-9:]) #last word

print(sentence.split()) # split sentence by delimiter(space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

print('\n'.join(sentence_split))

quoteception = "I said, \"Give me all the money\"" #\backslash- pozwala np. na wstawienie cudzysłowia w cudzysłowiu

letter= "a"
word= "Apple"
print(letter.lower() in word.lower()) #case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "           hello           "
print(too_much_space.strip())

full_name="at Black"
print(full_name.replace("at", "Mat"))

movie= "The Hangover"
print("My favourite movie is {}.".format(movie))

def favourite_book(title, author):
    fav= "My favourite book is \"{}\", which is written by {}.".format(title,author)
    return fav

#Dictionaries
print("Dictionaries are keys and values:")

drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple": 8} #drinks are keys and price is value

employees = {"Finane": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Paul", "Ace"]}

#List and dictionaries
movies= lista filmów
person= lista osob
combined = zip(movies,person)
movie_dictionary= {key: value for key, value in combined} #połączenie dwóch list w słownik. pierwsza lista do keys a druga to values
