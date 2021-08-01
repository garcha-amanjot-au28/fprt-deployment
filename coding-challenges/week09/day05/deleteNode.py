# Q-1 ) Delete Node in a Linked List
# Q-2 )Remove Duplicates from Sorted List

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

Head = None

# Ans1 : Delete Node with val = 3 in a Linked list 

def deletenode(val):

    global Head 
    if Head is None:
        return
    
    if Head.data == val and Head.next == None:
        Head = None
        return
    if Head.data == val and Head.next != None:
        Head = Head.next
    
    prev = Head
    curr = Head 

    while curr.next != None:
        if curr.data == val:
            node = curr
            curr = curr.next
            prev.next = node.next.next
            
        else:
            prev = curr
            curr = curr.next
        
# Ans-2 )Remove Duplicates from Sorted List
def removedups():
    global Head

    curr = Head 
        
    while curr :
        
        while curr.next and  curr.data == curr.next.data:
                curr.next = curr.next.next 
                
        
        curr = curr.next
    return Head



    

    

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

def removeVal(val):
    global Head
    if Head is  None:
        return   
    
    while Head.data == val and Head.next!= None :
         Head = Head.next

    if Head.data == val and Head.next == None:
        Head = None
        return
    
    

    
   
    prev = Head
    
    curr = Head
    while curr.next!= None:
        
        if curr.data == val:
            node = curr
            curr = curr.next
            prev.next = node.next
    
            

        else:   
            prev = curr
            curr = curr.next
    print(curr.data)
    if curr.data == val:
        curr = None

        
        
        

    

def PrintAll():
    global head 

    if Head is None:
        print('LInked List is Empty')
        return

    curr = Head
    
    while curr.next != None:
        print(curr.data)
        curr = curr.next
    print(curr.data)

addAtend(1)
addAtend(2)
addAtend(3)
addAtend(4)
addAtend(4)
addAtend(6)
PrintAll()
print()
deletenode(3)
PrintAll()
print()
removedups()
PrintAll()


