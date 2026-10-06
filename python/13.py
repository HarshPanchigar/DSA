s = "azyugyzaaaa"
q = ['a','z','y','u','d']

lst = list(s)

dict = {}
for i in lst:
    if i in q:
        dict[i] = dict.get(i,0) + 1

print(dict)