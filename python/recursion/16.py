# print i to n

def demo(i , n):
    if i > n:
        return
    print(i)
    demo(i+1,n)

i = int(input("Enter starting point : "))
n = int(input("Enter ending point : "))
demo(i , n)