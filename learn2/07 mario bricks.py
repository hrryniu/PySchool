def main():
    #print_column(3)  #funkcja tworząca bloki do peskakiwania
    #print_row(4)    #funkcja tworząca bloki do wskakiwania
    print_square(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# def print_row(width):
#     print("?" * width)

def print_square(size):
    for i in range(size):
        #print("#" * size)  #sposob ktory wymysliłem
        for j in range(size):
            print("#", end="")
        print() #stworzenie nowej linii



main()
