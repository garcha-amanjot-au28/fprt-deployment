# Q-2 ) Palindrome Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
head = None 

def isPalindrome():
    global head
    if head is None:
        return False
    if head.next is None:
        return True
    slow , fast , prev = head , head , None
    while fast and fast.next:
        slow , fast = slow.next , fast.next.next
    prev = slow 
    slow = slow.next
    prev.next = None
    while slow :
        temp = slow
        slow = slow.next
        temp.next = prev
        prev = temp 
    slow = prev
    fast = head
    while slow:
        if slow.data != fast.data:
            return False
        return True


    
def addatend(data):
    global head
    if  head == None :
        head = Node(data)
        return
    curr = head 

    while curr.next:
        curr = curr.next
    curr.next = Node(data)

        
def printAll():
    global head

    if not head:
        print('Linked List is Empty')
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

if __name__ == '__main__':
    
    addatend(1)
    addatend(2)
    addatend(2)
    addatend(1)
    printAll()
    print(isPalindrome())




