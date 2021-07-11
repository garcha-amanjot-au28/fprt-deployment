def searchRange( nums: list[int], target: int) -> list[int]:
        for start, i in enumerate(nums):
            if target == i:
                
                for last , n in reversed(list(enumerate(nums))):
                    if n == target:
                        a= [start,last]
                        return a
        b = [-1,-1]
        return b 

print(searchRange([1,1,2,4,5,6,6,6,7,8],6),end="")
                        