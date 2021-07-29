def nextLarger(nums):
    for i in  range (len(nums)-1):
        max = nums[i]
        for j in range (i+1,len(nums)):
            if nums[j] > nums[i]:
                nums[i] = nums[j]
                break
    nums[-1] = None

    print(nums)

nextLarger([2,1,7,4,6,8,1,9])