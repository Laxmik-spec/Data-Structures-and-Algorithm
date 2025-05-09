# Implementation of a stack using Queue

# using collections.deque
# Stacks in python are created by the collections module which provides a deque class
# append and pop operations are faster in deque than in list
# deque is a double-ended queue
# deque is a thread-safe, memory-efficient, and fast data structure
# deque is a generalization of stacks and queues

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print("Stack ", stack)
print(stack.pop())
print("Stack ", stack)

