class Treenode:
    def __init__ (self , data):
        self.data = data
        self.left = None
        self.right = None
        
best = 1
def diameterOfBinaryTree(root):

    def depth (root):
        global best
        if root == None:
            return 0

        ansL = depth(root.left)
        ansR = depth(root.right)

        best = max (best , ansL + ansR + 1)

        return 1 + max(ansL , ansR)

    depth(root)
    return best - 1


node = Treenode(1)
node.left = Treenode(2)
node.right = Treenode(3)
node.left.left = Treenode(4)
node.left.right = Treenode(5)

print(diameterOfBinaryTree(node))

