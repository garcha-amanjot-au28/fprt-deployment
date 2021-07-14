def lowerbound(nums,target):
    ans = 0
    left =0
    right = len(nums)-1

    while left <= right :
        mid = (left+right)>>1
        if nums[mid] == target:
            ans = mid
            right = mid-1
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1 
    return ans

def upperbound(nums,target):
    ans = 0
    left =0
    right = len(nums)-1

    while left <= right :
        mid = (left+right)>>1
        if nums[mid] == target:
            ans = mid
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1 


    return ans
ar =[1,2,2,2,3,3,3,3,4]
target = 3
print(lowerbound(ar,target),upperbound(ar,target))

