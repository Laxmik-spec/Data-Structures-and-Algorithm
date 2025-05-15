# Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.Preorder()
        if self.right:
            self.right.Preorder()
    
    def Inorder(self):
        if self.left:
            self.left.Inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.Inorder()
    
    def Postorder(self):
        if self.left:
            self.left.Postorder()
        if self.right:
            self.right.Postorder()
        print(self.data, end=' ')

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder Traversal:")
root.Preorder()
print("\nInorder Traversal:")
root.Inorder()
print("\nPostorder Traversal:")
root.Postorder()