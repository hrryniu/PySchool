from random import sample
moje_liczby={7,11,27,39,40,45}
totek_liska =range(1,50)

wylosowane_liczby=set()

while wylosowane_liczby != moje_liczby:
    wylosowane_liczby=set(sample(totek_lista,6))
    if moje_liczby == wylosowane_liczby:
        print('wygrałeś')

