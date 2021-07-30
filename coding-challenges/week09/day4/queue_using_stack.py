class MyQueue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []
        print('null')


    def push (self,x):

        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2 != []:
            self.stack1.append(self.stack2.pop())
        print('null')
            
    def pop (self):

        if self.stack1 != []:
            return self.stack1.pop()

    def peek (self):
        if self.stack1 != []:
            return self.stack1[-1]

    def empty (self):
        if self.stack1 == []:
            return True
        else:
            return False


obj = MyQueue() 

obj.push(1)

obj.push(2)

print(obj.peek())
print(obj.pop())
print(obj.empty())