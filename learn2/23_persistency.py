# names = []
#name= input("What's your name? ")

#with open("Names.txt", "a") as file:
#     file.write(f"{name}\n")
# with open("names.txt" , "r") as file:
#     lines= file.readlines()
#
# for line in lines:
#     print("hello," , line, end="")

# for _ in range(3):
#     names.append(input("What's your name? "))
#
# for name in sorted(names):
#     print(f"hello,{name}")

with open("names.txt") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip())