# Q-1 ) Write a program to remove first node from a linked list:
class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

Head = None

def removeAtBeg():# removes the head 
    global Head 
    if Head == None :
        return

    Head = Head.next


def addAtend(data):
    global Head
    if Head is None:
        Head = Node(data)
        return
    
    curr = Head
    while curr.next != None:
        curr = curr.next

    curr.next = Node(data)

def addAtbeg (data):
    global Head
    if Head is None:
        Head = Node(data)
        return
    
    tempnode = Head
    Head = Node(data)
    Head.next = tempnode

def AddAtindex(i,data):
    global Head
    if Head is None:
        Head = Node(data)
        return
    
    curr = Head
    counter = 1 
    while counter != i :
        curr = curr.next
        counter+=1

    tempnode = curr.next
    curr.next = Node(data)
    curr.next.next = tempnode
    



def removeAtend ():
    global Head
    if Head is  None:
        return
    
    curr = Head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None

def removeAtIndex(i):
    global Head
    if Head is  None:
        return
    
    counter = 1 
    curr = Head
    while counter != i:
        curr = curr.next
        counter+=1

    curr.next = curr.next.next

def PrintAll():
    global head 

    if Head is  None:
        print('LInked List is Empty')

    curr = Head
    
    while curr.next != None:
        print(curr.data)
        curr = curr.next
    print(curr.data)

addAtend(1)
addAtend(2)
addAtend(3)
addAtend(4)
addAtend(5)
PrintAll()
print()
removeAtBeg()
PrintAll()
