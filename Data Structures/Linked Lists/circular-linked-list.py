# Circular Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Inserting a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
    
    # Inserting a node after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if new_node.next == self.head:
            new_node.next = self.head
            