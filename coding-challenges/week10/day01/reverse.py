class Node:

    def __init__(self,x):
        self.data = x
        self.next = None 
head = None
def addatend(x):
    global head
    if head is None:
        head = Node(x)
        return
    curr = head 

    while curr.next :
        
        curr = curr.next
    curr.next = Node(x)


    


def printList(head):
    curr = head
    while curr :
        print(curr.data,end=" ")
        curr = curr.next

newhead = None
def reverse_rec(head, prev):
    global newhead

    if head is None:
        return
    elif head.next is None:
        head.next = prev
        return head
    
    newhead = reverse_rec(head.next,head)
    head.next = prev

    return newhead

if __name__ == "__main__":
    
    addatend(5)
    addatend(15)
    addatend(25)
    addatend(35)
    printList(head)
    print()
    head_rev = reverse_rec(head,None)
    printList(head_rev)


