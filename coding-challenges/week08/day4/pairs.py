def numIdenticalPairs( nums: list[int]) -> int:
        pair = 0
        for i in range (len(nums)):
            for j in range (i):
                if nums[i] == nums[j]:
                    pair+=1
                
        return pair

print(numIdenticalPairs([1,2,3,1,1,3]))
        