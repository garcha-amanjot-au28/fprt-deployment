# program to find n to the power m 
m= 5
def power(n:int):
    global m
    m = m-1
    if m == 0 :
        return n


    ans = n * power(n)
    return ans

print(power(5))