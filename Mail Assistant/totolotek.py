
from random import sample
moje_liczby = []
wybor=1
wybranka=int()
totek_lista=range(1,50)
wylosowane=sample(totek_lista,6)
print(wylosowane)
while wybor<=6:
    wybranka=input(f"Wybierz {wybor} liczbe z zakresu 1-49:")
    moje_liczby.append(wybranka)
    wybor+=1

print(f'Wybrane przez Ciebie liczny tp {moje_liczby}')

# if moje_liczby == wylosowane:
#     print('wygrales')
# else:
#     print('nie wygrales')
# print(moj_wybor)
# priny(x)