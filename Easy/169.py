nums = [2,2,1,1,1,2,2]

res = None
count = 0

for i , num in enumerate(nums):
    if count == 0:
        res = num
    print("No : ", i)
    print(f"Num : {num}, result : {res} ,count : {count}")
    if num == res:
        count += 1
    else:
        count -= 1
    print(f"Num : {num}, result : {res} ,count : {count}\n")

print(res)