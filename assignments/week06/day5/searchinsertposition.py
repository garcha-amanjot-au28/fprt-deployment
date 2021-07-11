def searchInsert(nums: list[int], target: int) -> int:
        
        if target > nums[-1]:
            return len(nums)
        
        for i in range (len(nums)):
            if target <= nums[i]:
                return i

print(searchInsert([1,3,5,7,9],8))
        