def sumofdigit (n : int):
    
    if n == 0:
        return 0

      
    return n%10 + sumofdigit(int(n/10))

print(sumofdigit(12345))




