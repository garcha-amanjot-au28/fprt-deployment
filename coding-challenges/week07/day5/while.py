# # Q-4 )[BONUS QUESTION] Write a while loop implementation of selection
# sort?

# 
arr= [80,100,400,2,90,40]
i=0
n = len(arr)
k = i +1


while i < n:
    min = i
    
    
    j= i+1
    while j < n:
        
        if arr[j] < arr[min]:
            min = j
        j+=1
    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp

    i += 1 
print(arr)

