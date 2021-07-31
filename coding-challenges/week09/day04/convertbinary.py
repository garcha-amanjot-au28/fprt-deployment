
# Q-2 ) Convert Binary Number in a Linked List to Integer:


class Node:

    def __init__(self, data):
        
        
        self.data = data
        self.next = None
        


head = None

def addatend(data):
    global head

    if head is None:
        head = Node(data)
        return

    curr = head

    while curr.next != None:
        curr = curr.next
    curr.next = Node(data)


def solution ():
    global head
    if head is None:
        return

    

    curr = head
    result = 0
    
    # Q2 # converts node binary numbers 101 to their decimal value of 5
    while curr.next != None:
        result = result * 2 + curr.data
        curr = curr.next
    result = result * 2 + curr.data

    return result
# Q-3 ) Middle of the Linked List
def retmiddle():

    global head
    
    a = middleval()
    
    curr = head 
    counter = 1 
    while counter != a:
        counter+=1
        curr = curr.next
    return curr.data
    
    
# to calculate the size of the linked list and return middle   
def  middleval ():
    global head 
    if head is None:
        return
    
    curr = head 
    counter = 1

    while curr.next != None:
        counter +=1
        curr = curr.next 
    

    
    middle = (counter//2) + 1

    
    return middle 




def printall():
    global head 

    if head is None :
        print ('Linked List is Empty')



    
    curr = head

    while curr.next !=None:
        print(curr.data)
        curr = curr.next
    print(curr.data)

addatend(1)
addatend(0)
addatend(1)
printall()
print()
print('decimal value of linked nodes is :' , solution())
print()

print('middle of linked list is :',retmiddle())