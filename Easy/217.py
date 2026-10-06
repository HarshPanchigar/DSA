# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# brute force
# nums = [1,2,3,1]
# freq = []
# for i in nums:
#     if i in freq:
#         print(True)
#         break
#     else:
#         freq.append(i)
# else:
#     print(False)

# Optimal solution 
nums = [1,2,3,1]
seen = set()

for i in nums:
    if i in seen:
        print(True)
        break
    seen.add(i)
else:
    print(False)