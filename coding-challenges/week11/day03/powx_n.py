
def myPow( x: float, n: int) :
    if n >= 0 :
        
    
    
        
        if n == 1 :
            return x
        if n == 0 :
            return 1

        ans = x * myPow(x,n-1)
        return ans
    else:
        n = abs(n)
        # if n == 1 :
        #     return x
        if n == 0 :
            return 1

        ans = x * myPow(x,n-1)
        return 1/ans
if __name__ == '__main__':
    print(myPow(2,-4))