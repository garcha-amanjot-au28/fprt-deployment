# Q - 1 ) Sort Array by Increasing Frequency (5 Marks)

# Given an array of integers nums, sort the array in increasing order based on the frequency of
# the values. If multiple values have the same frequency, sort them in decreasing order. Return
# the sorted array.
def frequencySort( nums: list[int]) -> list[int]:
 
    nums = sorted(nums,reverse=True)  #sorting the list in reverse order so values of same frequency display in decreasing  order
    a = {}  # putting values in dict to get their count 
    for i in nums:
        if i in a:
            a[i]+=1
        else: 
            a[i]=1
    

    a=(sorted(a.items(), key=lambda x: x[1])) # sorted a according to its values 
    

    # putting all keys in list times their frequency
    t = []
    for i in a:
        a, b = i
        t.extend([a] * b)
    return t

print(frequencySort([-1,1,-6,4,5,-6,1,4,1]))


        