# Q-1 ) write a program to take input a Binary tree and tell if that binary tree is
# balanced or not?
class Treenode:

    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

def check (node):
    if not node :
        return 0

    left = check(node.left)
    if left == -1 :
        return -1
    
    right = check(node.right)
    if right == -1 :
        return -1

    if abs (left-right) > 1:
        return -1

    return max (left,right)+ 1

def isBalanced(node):
    return check(node) != -1
    

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
# Q - 3) Merge Two Binary Trees
def mergeTrees(root,node):
      if not root or not node : return root  or node
      
      root1 = Treenode(root.data + node.data)
      root1.left = mergeTrees(root.left, node.left)
      root1.right = mergeTrees(root.right, node.right)

      return root1

node = Treenode(5)
node.left = Treenode(4)
node.right = Treenode(3)
node.left.left = Treenode(8)
node.left.right = Treenode(9)
inorder(node)
print()
print(isBalanced(node))

root = Treenode(8)
root.left = Treenode(7)
root.right = Treenode(2)
root.right.left = Treenode(2)
root.right.right = Treenode(12)

root1 = mergeTrees(root,node)
print()
inorder(root1)