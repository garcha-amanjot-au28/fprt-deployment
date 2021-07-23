def smallerNumbersThanCurrent( nums: list[int]) -> list[int]:
        a = []
        for index , i in enumerate(nums):
            sum = 0
            for j in range (len(nums)):
                if nums[j] < i and index != j:
                    sum+=1
            a.append(sum)
        return a


nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
