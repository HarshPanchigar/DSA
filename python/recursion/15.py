def greet(x , n):
    if n == 0:
        return
    print(x)
    greet(x,n-1)

greet(15,4)