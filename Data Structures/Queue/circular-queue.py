#  Circular Queue Implementation in Python

#  A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
#  In a circular queue, the last position is connected back to the first position to form a circle.
#  It is also called a ring buffer.
#  Circular queues are used in various applications such as CPU scheduling, memory management, and data buffering.
#  Circular queues are more efficient than linear queues because they use the available memory more effectively.
#  In a circular queue, the front and rear pointers are used to keep track of the first and last elements in the queue.
#  The front pointer points to the first element in the queue, and the rear pointer points to the last element in the queue.
#  When an element is added to the queue, the rear pointer is incremented, and when an element is removed from the queue, the front pointer is incremented.
#  When the rear pointer reaches the end of the queue, it wraps around to the beginning of the queue.
#  Similarly, when the front pointer reaches the end of the queue, it wraps around to the beginning of the queue.
#  This allows the circular queue to use the available memory more effectively.
#  The circular queue will have a fixed size, and the maximum size of the queue will be defined at the time of creation.
#  The circular queue will have the following operations:

#  1. Enqueue: Add an element to the rear of the queue.
#  2. Dequeue: Remove an element from the front of the queue.
#  3. Display: Display the elements in the queue.
#  4. Size: Return the number of elements in the queue.
#  5. IsEmpty: Check if the queue is empty.
#  6. IsFull: Check if the queue is full.
#  7. Front: Return the front element of the queue.
#  8. Rear: Return the rear element of the queue.


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.size == self.head):
            print("Queue is full")
            return
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = data
            
    def dequeue(self):
        if(self.head == -1):
            print("Queue is empty")
            return
        elif self.head == self.tail:
            data = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return data
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return data
        
    def display(self):
        if self.head == -1:
            print("Queue is empty")
            return
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
        print()


cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()

print("Dequeued element: ", cq.dequeue())
cq.display()
cq.enqueue(6)
cq.enqueue(12)
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()
cq.enqueue(7)
cq.enqueue(8)
cq.display()