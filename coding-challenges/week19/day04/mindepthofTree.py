class Node:

    def __init__ (self, key):
        self.data = key
        self.right = None
        self.left = None

    def minDepth (self, root):

        if root is None:
            return 0

        if root.right is None and root.left is None:

            return 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        if root.left is None:
            return self.minDepth(root.right) + 1

        return min (self.minDepth(root.left),self.minDepth(root.right)) + 1


if __name__ == '__main__':

    root = Node(2)
    root.right = Node(7)
    root.left = Node(4)
    root.right.right = Node(2)
    root.right.left = Node(1)
    root.left.left = Node(5)
    root.left.left.left = Node(9)

    print(root.minDepth(root))