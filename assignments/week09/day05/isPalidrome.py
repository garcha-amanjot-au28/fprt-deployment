class Node :

    def __init__ (self,data):
        
        self.data = data
        self.next = None

head = None

def isPalindrome():
    global head

    if head == None:
        return False
    if head.next == None:
        return True
    
    val = []

    val+= head.data,
    head = head.next

    return val == val[::-1]





def addatend(data):

    global head 

    if head is None :
        head = Node(data)

    curr = head 

    while curr.next:
        curr = curr.next
    curr.next = Node(data)


def PrintAll ():
    global head

    if head == None:
        print('inked list is empty')
        return
    
    curr = head 
    while curr :
        print (curr.data)
        curr = curr.next
    return


addatend(1)
addatend(2)
addatend(3)
addatend(4)
addatend(3)
addatend(2)
addatend(1)
PrintAll()
print()
print(isPalindrome())




