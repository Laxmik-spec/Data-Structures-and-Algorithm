
# creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating a class of Singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Inserting a node at the beginning, end, or after a given node
    
    # Inserting a node at the beginning 
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    # Inserting a node after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Deleting a node at the beginning, end, or after a given node

    # Deleting a node at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next

    # Deleting a node at the end
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Deleting a node after a given node
    def delete_after(self, prev_node):
        if prev_node is None or prev_node.next is None:
            print("The given previous node cannot be None or does not have a next node")
            return
        prev_node.next = prev_node.next.next


    # Traversing a linked list
    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
sll = SinglyLinkedList()

sll.head = node1
node1.next = node2
node2.next = node3

sll.insert_at_beginning(43)
sll.traverse()
sll.insert_at_end(490)
sll.traverse()
sll.insert_after(node2, 100)
sll.traverse()

sll.delete_at_beginning()
sll.traverse()
sll.delete_at_end()
sll.traverse()
sll.delete_after(node1)
sll.traverse()
