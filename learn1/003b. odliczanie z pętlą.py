from time import sleep

for odliczenie in [10,9,8,7,6,5,4,3,2,1]:
    print(odliczenie)
    if odliczenie > 3:
        sleep(1)
    else:
        sleep(2)

print("KABOOM!!!")
