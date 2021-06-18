num = int(input("Please enter a number:"))
a = num + 2
b=1
c=num-2
if not num%2 ==0 :
    for i in range (1,num+1):
        for n in range (a-2):
            print("*",end="")
        print("")
        
        print("\n")
        a=a-2
        if a==1:
            break
        print(" "*(b),end="")
        b=b+1
        

    
    c=1
    d=num//2

    for l in range (num):
        print(" "*(d),end="")

        for j in range (c+l):
            print("*",end="")
        d-=1
        c+=1
        if d == -1:
            break
        print("")
        print("\n")
        
    
        

   
    
    
    
        
        
    
        
        
        
    

            
else:
    print("Not an odd number")