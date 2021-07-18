# Q-3 ) Write a program perform selection sort using an auxiliary (extra) list,
# and tell the time complexity and space complexity of your code. (5 marks)


a = [2,5,4,80,75]
arr = []
n = len(a)
for i in range (n):
    arr.append(a[i])
    

for j in range (n):
        min = j
        for k in range (j+1,n):
            if arr[k]<arr[min]:
                min = k
        temp = arr[min]
        arr[min] = arr[j]
        arr[j] = temp
print(arr)
        

#  time complexity = o(n2)
# space complexity = o(n)


            
    

