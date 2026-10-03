n = [1, 2, 2, 3, 1, 2, 3]

dict = dict()
x = 1
for i in n:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)
print(dict[x])