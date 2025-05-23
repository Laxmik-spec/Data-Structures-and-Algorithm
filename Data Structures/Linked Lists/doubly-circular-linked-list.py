# Cirular Linked List
# A circular linked list is a linked list where all nodes are connected in a circle.
# There is no NULL at the end of the list. The last node points to the first node instead of NULL.
# This means that the list can be traversed from any node and will eventually return to that node.
# This is useful for applications that require a circular traversal of the list, such as in a round-robin scheduling algorithm.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        # Initialize the head of the list to None
        # The head will point to the first node in the list
        # If the list is empty, the head will be None
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        else:
            current = self.head
            print('Forward Traversal:')
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("None")

    def backward_traversal(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        else:
            current = self.head
            print('Backward Traversal:')
            while True:
                print(current.data, end=" -> ")
                current = current.prev
                if current == self.head:
                    break
            print("None")

    # Inserting a node at the beginning, end, or after a given node

    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    # Inserting a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node

    # Inserting a node after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node
            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node

    # Deleting a node
    def delete_node(self, node):
        if self.head is None or node is None:
            print("Circular Linked List is empty or the given node cannot be None")
            return
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


    # Deleting a node at the beginning, end, or after a given node
    # Deleting a node at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    # Deleting a node at the end
    def delete_at_end(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head.prev
            last.prev.next = self.head
            self.head.prev = last.prev
    
    # Deleting a node after a given node
    def delete_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("The given previous node cannot be None or has no next node")
            return
        else:
            node_to_delete = prev_node.next
            prev_node.next = node_to_delete.next
            node_to_delete.next.prev = prev_node

    
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1
n1.prev = n4
n2.prev = n1
n3.prev = n2
n4.prev = n3
cll = CircularLinkedList()
cll.head = n1
cll.insert_at_beginning(50)
cll.insert_at_end(20)
cll.insert_after(n1, 30)

cll.delete_at_beginning()
cll.delete_at_end()
cll.delete_after(n1)

cll.forward_traversal()
cll.backward_traversal()