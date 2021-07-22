def maxAscendingSum( nums: list[int]) -> int:
        
        i = 0
        
        res= 0

        sum = 0
        
        
            
        while i <len(nums):
            
            
            if i == 0 or nums[i]>nums[i-1]:
                sum += nums[i]
                
            else:
                sum = nums[i]
                
            res = max(sum,res)
            i+=1
            
        return res

print(maxAscendingSum([12,17,15,13,10,11,12]))