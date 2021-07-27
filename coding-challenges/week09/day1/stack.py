def perfect(string):
    stack = []
    dict = { ")":"(" , "}":"{","]":"["}

    for i in string:
        


        if i in dict:
            if stack == [] or dict[i] != stack.pop():
                return False
            
            
        
        else:
            stack.append(i)
            
            

    
    return stack == []

    # else: 
    #     False

print (perfect("(([]))"))

    