class Solution:
    def prob(self,nums:list[int], k : int):
            n = len(nums)
            num = []
            for i in range (n):
               a=  nums[i-k] 
               
               num.append(a)
               
            return num 

            
               
    
            
               
               


result = Solution()
print(result.prob([1,2,3,4,5,6,7],3))



            
