# Q-3 )Remove All Adjacent Duplicates In String (5
def removeDuplicates( s: str) -> str:
        stack = []
        
        for i in s:
            
           
                
            if stack != [] and stack[-1] == i:
                    stack.pop()
               
            else:
                
                stack.append(i)
                
        d = ''.join(stack)
        return d

print(removeDuplicates('abbbabaaa'))