def sortedSquares(nums: list[int]) -> list[int]:
    a=[]
    for i in range (len(nums)):
        a.append(nums[i]*nums[i])
        # print(a)
        
    
    return sorted(a)



print(sortedSquares([-7,-3,2,3,11]))