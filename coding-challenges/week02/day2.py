print("Please enter a value for a:")
a = int(input("a = "))
print("Please enter a value for b:")
b = int(input("b = "))
print("Please enter a value for c:")
c = int(input("c = "))
print("A = ", a)
print ("b = ", b)
print ("c = ", c)
print("Largest number:")
if  a>b and a>c:
    print ("a", a)
elif a==b and a>c:
    print ("a = ", a ,"and b =", b)
elif a==c and a>b:
    print("a =",a ,"and c = ", c)
elif b>a and b>c :
        print ("b =", b)
elif b==c and b>a:
    print ("b =", b ,"and c =", c)
elif  c>a and c>b:
            print("c =", c)
else:
    print ("All numbers equal")


