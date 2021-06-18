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
        print(" "*(b),end="")
        b=b+1
        a=a-2
        if a==1:
            break
    print("\n")
    for l in range (c):
        for j in range(1,c-l):
            
            print(" ",end="")
        for k in range(2*l+1):
            print("*",end="")
        print("")
        print("\n")
        
    
        
        
        
    

            
else:
    print("Not an odd number")