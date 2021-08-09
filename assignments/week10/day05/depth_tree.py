# Q-3) Maximum Depth of Binary Tree(or height of a BT): (
class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def maxdepth(root):
    if not root :
        return 0
    else:
        return 1 + max (maxdepth(root.left), maxdepth(root.right))

def insert(arr,root,i,n):
    if i < n :
        temp = Treenode(arr[i])
        root = temp
        root.left = insert(arr,root.left,2*i + 1,n)
        root.right = insert(arr,root.right,2*i + 2, n)
    return root

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)

# def preorder(root):
#     print(root.data)
#     preorder(root.left)
#     preorder(root.right)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    i = 0 
    n = len(arr)
    root = None
    root  = insert(arr,root,i,n)
    # inorder(root)
    # print()

    # postorder(root)
    # print()
    print(maxdepth(root))