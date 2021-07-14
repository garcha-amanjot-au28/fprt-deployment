def mySqrt( x: int) -> int:
        
    start = 0
    end = x 
    while start <= end:
        mid = (start+end)//2
        if mid**2 == x :
            return mid 
        elif x < mid**2 :
            end = mid -1
        else:
            start = mid+1
        
    return end 

print(mySqrt(8))