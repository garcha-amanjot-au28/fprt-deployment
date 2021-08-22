
def totalNQueens( n):
    """
    :type n: int
    :rtype: int
    """
    
   
    
    
    def helper( n, diag1, diag2, usedCols, row):
        if row == n:
            return 1
        
        solutions = 0
        
        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in usedCols:
                continue
                
            diag1.add(row + col)
            diag2.add(row - col)
            usedCols.add(col)
            
            solutions += helper(n, diag1, diag2, usedCols, row + 1)
        
            diag1.remove(row + col)
            diag2.remove(row - col)
            usedCols.remove(col)
        
        return solutions
    diag1 = set()
    diag2 = set()
    usedCols = set()
    return helper(n, diag1, diag2, usedCols, 0)


if __name__ == '__main__':
    n = 4
    print(totalNQueens(n))

