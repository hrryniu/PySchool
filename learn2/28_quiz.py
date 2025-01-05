print("Welcome to my computer quiz!")

playing= input("U wanna play my game? ")
if playing.lower() != "yes":
    quit()

print("okay! Let's play ;)")
score = 0

answer =  input("What does CPU stand for? ")
if answer.lower() == "Central Processing Unit":
    print("Correct!")
    score +=1
else:
    print("Nah! Wrong")

answer =  input("What does RAM stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

answer =  input("What does PSU stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

answer =  input("What does GUI stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

answer =  input("What does ROM stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

answer =  input("What does UI stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

answer =  input("What does OS stand for? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Nah! Wrong")

print(f"You got {score} correct answers!")
print("You got "+str((score/7)*100)+ "%.")