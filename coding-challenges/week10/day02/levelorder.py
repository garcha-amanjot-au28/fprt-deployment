def insert(arr,root,i,n):
    if i < n :
        temp = Tree(arr[i])
        root = temp
        root.left = insert(arr,root.left,2*i + 1,n)
        root.right = insert(arr,root.right,2*i +2,n)
    return root

def levelOrder(root):
    h = height (root)
    for i in range(1, h+1): 
        printElementsinLevel(root,i)

def printElementsinLevel(root,level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level>1:
        printElementsinLevel(root.left,level-1)
        printElementsinLevel(root.right,level-1)
        

