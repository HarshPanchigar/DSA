def arrsum(s, i , n):
    if i > n:
        print(s)
        return
    arrsum(s + i, i+1,n)

arrsum(0,1,4)