

count = 0

def length (n: str):
    global count
    
    if n == "":
        return ""
    else:
        count += 1

        length(n[1:])
    return count
    
    

    

    
print(length("aman"))


    
    
    



    



