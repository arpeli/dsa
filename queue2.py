# Loise Wambui
# QUEUES IN PYTHON
# Demonstrates FIFO (First In, First Out) data structure

# 1. Using list - Inefficient (O(n) for dequeue)

q = []
q.append('a')
q.append('b')
q.append('c')

print("Initial queue (list):", q)

print("Elements dequeued from queue:")
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print("Queue after removing elements:",q)


# 2. Using collections.deque - Efficient (O(1) for both operations)

from collections import deque
q = deque()

q.append('a')
q.append('b')
q.append('c')

print("Initial queue (deque):", q)

print("Elements dequeued from the queue:")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("Queue after removing elements:", q)


# 3. Using queue.Queue - Thread-safe for multi-threaded applications

from queue import Queue
q = Queue(maxsize=3)
print("Initial size:", q.qsize())

q.put('a')
q.put('b')
q.put('c')

print("Is full:", q.full())

print("Elements dequeued from the queue:")
print(q.get())
print(q.get())
print(q.get())

print("Is empty:", q.empty())

q.put(1)
print("Is empty:", q.empty())
print("Is full:", q.full())
