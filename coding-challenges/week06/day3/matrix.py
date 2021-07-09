lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# above is a 4 × 4 square matrix 


# Q.1  code to print the sum of its right diagonal 
sum = 0

for row in range (len(lst)):
    a = lst[row][len(lst)-row-1]
    sum = sum + a

print("Sum of right diagonal of lst = ", sum)

# Q.2 Program to print the border elements of a square matrix

row = 0
col = 0
sum = 0


while col < 4:
    a =lst[row][col]
  
    sum= sum + a
    
    col += 1

col-= 1
row += 1
while row < 4:
    a=lst[row][col]
    
    sum= sum + a
   
    row+=1


row -=1
col-=1
while col >= 0 :
    a=lst[row][col]
   
    col -= 1
    sum = sum +a
    

col+=1
row-=1
while row>=1:
    a=lst[row][col]
 
    sum= sum + a 
    row-=1


print("sum of corner elements of sqaure matrix lst is :",sum)

# Q.3 Program to print the sum of rows of a matrix as a list 

Sum=[]

for i in range (len(lst)):
    total=0
    for j in range (len(lst[0])):
        a = lst[i][j]
        
        total= total + a
    Sum.append(total)
print("Sum  of all rows as a list : ", Sum)



