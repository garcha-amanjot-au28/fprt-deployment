class MinStack:

    def __init__(self):

        self.normalstack = []
        self.minstack    = []
        
        

    def push (self,val):
        self.normalstack.append(val)

        if self.minstack != [] :
            self.minstack.append(min(self.minstack[-1],val)) 
            # append minstack smaller of top ele in minstack or current val
        else:
            self.minstack.append(val)

    def pop (self):
        self.normalstack.pop()
        self.minstack.pop()

    def top (self):
        return self.normalstack[-1]

    def getmin (self):
        return self.minstack[-1]


result = MinStack()
result.push(-2)
result.push(0)    
result.push(-3)

print(result.getmin())
result.pop()
print(result.top())    
print(result.getmin())
    
        
    


    