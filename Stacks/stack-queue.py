# Implementation of a stack using a queue

# Queue module contains the LIFO queue
# It has some additional and works same as stack
# put function is used to insert data
# get function is used to remove data

# Functions avaliable in queue module
# 1. empty() - returns true if the queue is empty
# 2. full() - returns true if the queue is full
# 3. get() - removes and returns an element from the queue
# 4. put() - adds an element to the queue
# 5. qsize() - returns the number of elements in the queue
# 6. task_done() - indicates that a formerly enqueued task is complete
# 7. join() - blocks until all items in the queue have been gotten and processed
# 8. maxsize - returns the maximum size of the queue
# 9. queue - returns the queue
# 10. put_nowait() - adds an element to the queue without blocking
# 11. get_nowait() - removes and returns an element from the queue without blocking

from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)
print(stack.full())
print(stack.qsize())
print("Stack ", stack.queue)
print(stack.get())
print("Stack ", stack.queue)
