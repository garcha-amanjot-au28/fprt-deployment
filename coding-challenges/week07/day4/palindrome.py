rev =0
p=0

def palindrome( n :int):
    global rev 
    global p
    if n < 0 :
        return False
    
    
    p = n 
    if p == 0 :
        return True


    rev = rev * 10 + p %10 
    palindrome(p//10)
    if rev == n :
        return True
    else: return False

    


print(palindrome(12321))