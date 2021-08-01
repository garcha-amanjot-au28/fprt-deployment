# Q-1 ) Implement Queue using Stacks
class Queue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []
        print('null')
    def push (self, x : int):

        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2 != []:
            self.stack1.append(self.stack2.pop())
        print('null')
    def pop(self):

        if self.stack1 != self.empty():
            return self.stack1.pop()

    def peek(self):
        if self.stack1 != self.empty():
            return self.stack1[-1]
        else :
            return -1


    def empty(self):

        if self.stack1 == []:
            return True
        else:
            return False
        
            



res = Queue()
res.push(1)
res.push(2)
print(res.peek())
print(res.pop())
print (res.empty())


    

