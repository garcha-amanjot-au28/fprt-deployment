def peak(nums) :
    left = 0
    right = len(nums)-1

    while left <right:
        mid = (left+right)//2
        mid1 = mid +1
        
        if nums[mid] < nums[mid1]:
            left = mid1
        else :
            right = mid 
    return left
ar = [1,2,3,4,3]
print(peak(ar))