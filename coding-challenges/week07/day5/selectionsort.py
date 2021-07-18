# Q-1 ) Select the appropriate code that performs selection sort.
#  Ans = a
def selection_Sort(arr: list[int]):
    n = len(arr)
    for j in range (n):
        min = j
        for k in range (j+1,n):
            if arr[k]<arr[min]:
                min = k
        temp = arr[min]
        arr[min] = arr[j]
        arr[j] = temp
    
    return arr


print(selection_Sort([2,5,4,8,10]))
    