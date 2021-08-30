class Node:
    
    def __init__(self,data):
        self.next = None
        self.data = data

def removeDup (head):
    
    if head is None:
        return
    curr = head
        
    while curr :
        
        while curr.next and  curr.data== curr.next.data:
                curr.next = curr.next.next 
            
        
        curr = curr.next
    return head

def printAll(head):
    
    if head is None:
        print("linked list is empty")
    else:
        curr = head
        while curr.next != None:
            print(curr.data)
            curr = curr.next
        print(curr.data)




if __name__ == '__main__':

    n = Node(5)
    n.next = Node(6)
    n.next.next = Node(6)
    n.next.next.next = Node(7)
    removeDup(n)
    printAll(n)


