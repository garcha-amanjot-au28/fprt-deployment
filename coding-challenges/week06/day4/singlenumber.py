nums = [4,1,2,1,2]
dup = []
# class Solution :
#     def singleNumber (self, nums: list[int])  ->    int:
count = {}
for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1


for x in count:
            if count[x] == 1:
               print(x)

        
        

    




