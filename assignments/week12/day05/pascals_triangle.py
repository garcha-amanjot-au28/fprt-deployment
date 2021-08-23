def generate(numRows):

    if numRows == 0 :
        return []

    res = [ [1] * (i+1) for i in range (numRows)]

    for row in range (2 , numRows):

        for col in range (1,row):

            res[row][col]  = res[row-1][col-1] + res[row-1][col]

    return res 


if __name__ == '__main__':

    print(generate(5))