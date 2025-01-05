
name= input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer= input("you're on a dirt road, it has come to an end and You can go left of right. Which way would You choose?")
if answer == "left":
    answer= input("You come to a river, you can walk around it or swim across. Type walk or swimm")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died.")
    else:
        print("Not a valid option. You lose")
elif answer == "right":
    print()
else:
    print("Not a valid option. you lose.")