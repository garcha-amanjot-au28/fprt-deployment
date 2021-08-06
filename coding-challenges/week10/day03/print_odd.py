class Tree:

    def __init__ (self,data):
        
        self.data = data
        self.right = None
        self.left = None

# Q-1 ) Write a program to print nodes in a BST having odd values:
def inOrderodd(root):
    if root :
        inOrderodd(root.left)
        if root.data % 2 != 0:# it will print all odd values in the tree
            print(root.data)
        inOrderodd(root.right)
# Q-2 ) Binary Search Tree to Greater Sum Tree Answer in the following function
Sum = 0
def bstToGst( root):
    global Sum  
        
    if root:
        
        
        bstToGst(root.right)

        Sum += root.data
        root.data = Sum


        bstToGst(root.left)
    return root   
count= []
def findSmall(root):
    global count
    if root:
        
        
        findSmall(root.left)
        count.append(root.data)
        findSmall(root.right)
# Q-3 ) Kth Smallest Element in a BST
def Smallestindex (root,k):
    global count
    findSmall(root)
    return count[k-1]

    

def inOrder(root):
    if root is None:
        return None
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def insertBst (root,data):
    if root == None:
        root = Tree(data)
        return root 
    if root.data < data:
        root.right = insertBst(root.right, data)

    else:
        root.left = insertBst(root.left, data )
    return root 





if __name__ == "__main__":
    
    arr = [8,3,1,6,4,7,10,14,13]
    root = None

    for i in arr:
        root = insertBst(root,i)
    
    inOrderodd(root)
    print()
    bstToGst(root)
    inOrder(root)
    print()
    print(Smallestindex(root,1))

        

