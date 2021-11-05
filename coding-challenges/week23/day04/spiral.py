class Matrix:
    def __init__ (self,n):
        self.n = n

    def buildmatrix (self):
        n = self.n
        matrix = [[0 for i in range(n)] for i in range (n)]

        value = 2
        matrix[0][0] = 1
        base = 0
        row = 0
        col = 1
        end = n*n
        while value <= end:
                
                while col < n and value <= end:
                    
                    matrix[row][col] = value
                    col +=1
                    value +=1
                col-=1
                row+=1
                while row < n and value <= end:
                    matrix[row][col] = value
                    row +=1
                    value +=1
                row-=1
                col-=1
                while col >= base and value <= end:
                    matrix[row][col] = value
                    value+=1
                    col-=1
                col+=1
                row-=1
                
                while row > base and value <= end:
                    matrix[row][col] = value
                    value+=1
                    row-=1
                row += 1
                col += 1
                base += 1
                n -= 1
                
                
        return matrix


            
if __name__ == '__main__':

    res = Matrix(4)
    print("Spiral Order Matrix for n = ",res.n,"is printed below : " )
    print(res.buildmatrix())
    res2 = Matrix(int(input("Please enter value of n = ")))
    print("Spiral Order Matrix for n = ",res2.n,"is printed below : " )
    print(res2.buildmatrix())