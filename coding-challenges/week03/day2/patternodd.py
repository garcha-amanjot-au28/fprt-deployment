num = int(input("Please enter a number:"))
a = num + 2
b=1
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
        
        
        
    

            
else:
    print("Not a odd number")