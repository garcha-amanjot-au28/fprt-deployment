a =  [[1,34,26], [22, 90, 37], [12, 44, 55], [56, 77, 88]]

Sum_1st_row = a[0][0]+a[0][1]+a[0][2]
print("Sum of rows :",Sum_1st_row)

Sum_3rd_Col = a [0][2] +a[1][2]+a[2][2]+a[3][2]
print("Sum of Colunms:",Sum_3rd_Col)

m = 4 
n= 3 
#since A is not a square matrix , i will will print the diagnol of first 3 rows
i = 0 
print("Diagonal elements of 1st 3 row are :")
for j in range (3):
    
        print(a[j][i],end=",")
        
        if i < 2:
            i+=1
