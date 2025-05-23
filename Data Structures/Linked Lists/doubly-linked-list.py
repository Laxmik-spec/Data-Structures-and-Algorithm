# Doubly Linked List Implementation in Python

class Node:
    def __init__(self, data):

        # Initialize a node with data, next pointer, and previous pointer
        # The next pointer points to the next node in the list
        # The previous pointer points to the previous node in the list
        # The next and previous pointers are initially set to None

        self.data = data
        self.next = None
        self.prev = None



class DoublyLinkedList:
    def __init__(self):
        # Initialize the head of the list to None
        # The head will point to the first node in the list
        # If the list is empty, the head will be None

        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        else:
            current = self.head
            print('Forward Traversal:')
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def backward_traversal(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        else:
            current = self.head
            print('Backward Traversal:')
            while current.next:
                current = current.next
            while current:
                print(current.data, end=" -> ")
                current = current.prev
            print("None")


    # Inserting a node at the beginning, end, or after a given node

    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Inserting a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Inserting a node after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Deleting a node at the beginning, end, or after a given node

    # Deleting a node at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    # Deleting a node at the end
    def delete_at_end(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    # Deleting a node after a given node
    def delete_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("The given previous node cannot be None or does not have a next node")
            return
        prev_node.next = prev_node.next.next
        if prev_node.next is not None:
            prev_node.next.prev = prev_node



n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2

n2.next = n3
n2.prev = n1

n3.next = n4
n3.prev = n2

n4.prev = n3

dll = DoublyLinkedList()
dll.head = n1

dll.insert_at_beginning(5)
dll.insert_at_end(50)
dll.insert_after(n2, 25)

dll.delete_at_beginning()
dll.delete_at_end()
dll.delete_after(n2)

dll.forward_traversal()
dll.backward_traversal()

