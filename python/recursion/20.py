def rev(arr, left , right):
    while left <= right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1
        return rev(arr, left, right)
    
    return arr


print(  rev([5, 9 , 8 , 3 , 6 , 7 , 1 , 4 , 2], 0 ,8))
print([2, 4, 1, 7, 6, 3, 8, 9, 5])