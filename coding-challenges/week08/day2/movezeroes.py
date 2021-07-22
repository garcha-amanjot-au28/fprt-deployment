def moveZeroes( nums: list[int]) -> None:
        
    for i in range (1,len(nums)):
        anchor = nums[i]
        j = i-1
        while j >=0 and nums[j]==0 :
            nums[j+1] = nums [j]
            j-=1
        nums[j+1]=  anchor

    print(nums)

moveZeroes([0,1,0,3,12])
