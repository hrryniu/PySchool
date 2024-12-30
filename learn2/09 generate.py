from random import choice
#import random

#przy importowaniu całej biblioteki muszę potem wpisać biblioteka.funkcja(random.choice)
#przy importowaniu pojedynczej funkcji można potem wpisać tylko funkcję- choice

coin = choice(["Heads", "Tails"])
#coin = random.choice(["Heads", "Tails"])

print(coin)

