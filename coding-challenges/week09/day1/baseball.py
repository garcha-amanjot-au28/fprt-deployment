# Q-2 )Baseball Game:
def calPoints( ops: list[str]) -> int:
        rec = []
        
        for i in ops:
            
            if i == "C":
                rec.pop()
                
            elif i == "D":
                rec.append(rec[-1] * 2)
                
            elif i == "+":
                
                rec.append(rec[-1]+rec[-2])
            else:
                rec.append(int(i))
        
        return sum (rec)


print(calPoints(["5","-2","4","C","D","9","+","+"]))