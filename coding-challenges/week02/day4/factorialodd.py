factorial = 1
number = int(input("Please enter a number :"))
if not number%2 == 00:
    for i in range(1,number+1):
        factorial = factorial*i
    print(factorial) 

else:
       print("even") 
  