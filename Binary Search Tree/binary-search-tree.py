# Binary Search Tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)
    def inorder(self):
        return self._inorder_rec(self.root)
    def _inorder_rec(self, root):
        return self._inorder_rec(root.left) + [root.val] + self._inorder_rec(root.right) if root else []
    def preorder(self):
        return self._preorder_rec(self.root)
    def _preorder_rec(self, root):              
        return [root.val] + self._preorder_rec(root.left) + self._preorder_rec(root.right) if root else []
    def postorder(self):
        return self._postorder_rec(self.root)
    def _postorder_rec(self, root):
        return self._postorder_rec(root.left) + self._postorder_rec(root.right) + [root.val] if root else []
    def search(self, key):
        return self._search_rec(self.root, key)
    def _search_rec(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root
    
root = BinarySearchTree()
root.insert(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)
print("Inorder traversal of the given tree")

print(root.inorder())
print("Preorder traversal of the given tree")
print(root.preorder())      
print("Postorder traversal of the given tree")
print(root.postorder())
print("Search for 40 in the tree")
print(root.search(40).val if root.search(40) else "Not found")
print("Delete 20")
root.delete(root.root, 20)
print("Inorder traversal after deletion")
print(root.inorder())
