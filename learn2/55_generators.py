#sleep
def main():
    n= int(input("What's n? "))
    for s in range(n):
        print(s)

def sheep(n):
    #flock = []
    for i in range(n):
    #    flock.append("🐑"* i)
    #return flock
        yield "🐑" * i
#yield to taki return ale nie wydaje całego wyniku od razu
# tylko dzieli to na mniejsze kawałki
#dzieki temu nie zapchamy pamięci



if __name__ == "__main__":
    main()