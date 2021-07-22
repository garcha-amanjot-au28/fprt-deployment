def reverseString( s: list[str]) -> None:
        
    n= len(s)-1
    
    mid = len(s)//2
    i = 0
    
    while i < mid:
        s[i],s[n]= s[n],s[i]
        i+=1
    print(s)



reverseString([1,2,3,4,5])
