n = [5, 3, 2, 2, 1, 5,5, 7,5, 10]
m = [10, 111, 1, 9,5, 67,27]

hash_list = [0] * 11

for i in n:
    hash_list[i] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])

# print(hash_list)



# hash = {}

# for num in m:
#     count = 0
#     for x in n:
#         if num == x:
#             count += 1

#     hash[num] = count

# print(hash)