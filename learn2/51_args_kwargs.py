def f(*args, **kwargs):
    print("Positional:", args)

f(100,50,25,5)

#dzieki temu mozemy podać dowolną ilośc argumnentów i
# funkcja *args to przyjmie i nie będzie błędu