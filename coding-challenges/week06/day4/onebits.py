# function that takes an unsigned integer and returns the number of '1' bits it has 
# (also known as the Hamming weight).
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        mask=1
        for i in range(32):
            if n & mask !=0 :
                count+=1
            mask<<=1
        return count    

    



