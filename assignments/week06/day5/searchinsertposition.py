def searchInsert(nums: list[int], target: int) -> int:
        
        
        
    start = 0
    end = len(nums)-1
    if target > nums[-1]:
        return len(nums)
    elif target < nums[0]:
        return 0 
    
    
    
    mid = int((start + end)/2)
        
    if target == nums[mid]:
            return mid
        
    elif target < nums[mid] :
            for i in range(start,mid+1):
                if target <= nums[i]:
                    return i
    else:
            for i in range (mid,len(nums)):
                if target <= nums[i]:
                    return i
    

print(searchInsert([1,3,5,7,9],8),end="")
    