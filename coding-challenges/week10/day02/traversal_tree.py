# Q-1 ) Maximum Depth of Binary Tree:

class Tree:

    def __init__ (self,x):

        self.data = x
        self.left = None
        self.right = None



def maxDepth( root: Tree) -> int:
        
        
        if root is None:
            
            return 0
        
        else:
            return 1+max (maxDepth(root.left), maxDepth(root.right))



def preorder(root):

    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
#Ans:2 postorder
def postorder(root):
    # A function to do postorder tree traversal

 
    if root:
 
        # First recur on left child
        postorder(root.left)
 
        # the recur on right child
        postorder(root.right)
 
        # now print the data of node
        print(root.data),
 
n = Tree(5)
n.left = Tree(4)
n.right = Tree(6)
n.left.left = Tree(5)
n.left.right = Tree(5)

preorder(n)
print()
postorder(n)
print()
print(maxDepth(n))
        
