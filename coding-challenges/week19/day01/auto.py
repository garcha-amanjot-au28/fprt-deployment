v=int(input("Please enter total number of vehicles : " ))
w=int(input("Please enter total number of four wheelers: "))
if (w&1)==1 or w<2 or w<=v:
    print("INVALID INPUT")
else:
    x=((4*v) -w)//2
    print("TW={0} FW={1}".format(x,v-x))