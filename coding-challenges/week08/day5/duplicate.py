def dup (nums):
    left = 0 
    right = len(nums)-1
    mid = (left+ right)//2
    while left < right:
        count = 0 
        for k in nums:
            if mid < k <= right:
                count+=1
        if count > right - mid :
            left = mid + 1
        else :
            right = mid 
        mid = (left + right )//2
    return right

print (dup([3,1,3,4,2]))
