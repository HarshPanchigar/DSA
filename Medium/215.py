nums = [3,2,3,1,2,4,5,5,6,90]

larg = nums[0]
for i in range(1,len(nums)):
    if nums[i] > larg:
        larg = nums[i]
print(larg)