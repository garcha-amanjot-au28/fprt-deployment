
num = int(input("Please enter a number:"))


if not num<=1:
    for i in range(2, num+1):
        
            for n in range(2, i):
                if (i % n) == 0:
                    break
            else:
                        print(i)
            
       
else:
     print("No prime number")       
