def product(x: int , y: int):
    if y == 0 :
        return 0


    return x + product(x,y-1)


print(product(10,3))