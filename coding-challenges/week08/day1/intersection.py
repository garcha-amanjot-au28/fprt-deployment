
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums3 = []
    for i in range (len(nums1)):
        for n in range (len(nums2)):
            if nums1[i] == nums2[n] and nums1[i] not in nums3:
                nums3.append(nums1[i])
                break
    
    return nums3


a = [2,3,5,8,9]
b = [8,4,5,6,7]

print (intersection(a,b))