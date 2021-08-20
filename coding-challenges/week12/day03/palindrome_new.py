
def isPalindrome( x: int) :
        
        
        
        
        if x < 0  or (x % 10 == 0 and x != 0):
            return False
        
        
        rev = 0
        
         
        
        while x > rev :
            
            rev = rev * 10 + x % 10
            x//=10

            
            
        if x == rev or x == rev//10:
            return True
            
        
        if x >= 0 and x <= 9 :
            return True

if __name__ == '__main__':

    print(isPalindrome(121))