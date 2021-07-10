def search(nums: list[int], target: int) -> int:
        mid = 0
        start = 0 
        end = len(nums)-1
        
        while start <= end:
            mid = int((start+end)/2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                end = mid -1
                
        return (-1)


a = search([1,3,5,6,8,9],3)
print(a)