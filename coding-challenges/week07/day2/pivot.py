def pivotIndex( nums):
    '''
    brute force, TC: O(n**2), SC: O(1)
    '''
    for i in range(len(nums)): #O(n)
        left = sum(nums[j] for j in range(i)) #O(n)
        right = sum(nums[j] for j in range(i+1,len(nums))) #O(n)
        if left==right:
            return i
    return -1


print(pivotIndex([1,2,3,4,3,3]))