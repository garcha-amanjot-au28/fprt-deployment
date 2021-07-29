# Q-1 ) Next Greater Element
def  nextGreater (nums):

    index = []  # stack for index number
    stack = []  # stack for getting next greater element

    for i , val in enumerate(nums):

        while stack != [] and stack[-1] < val:

            stack.pop()             # pop the smaller number 
            nums[index.pop()] = val # pop the index as well input the correct val in nums at same index

        stack.append(val)
        index.append(i)

    while index != []:
        nums[index.pop()] = -1      # replace last ele and ele not having a next greater val to right with -1 

    return nums

print(nextGreater([6,8,0,1,3]))