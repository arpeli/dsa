# Data Structures and Algorithms
Further information on [Applications of Data Strcutures and Algorithms](applications.md) as part of the assignment

## Overview
This specific docs explores various data structures and algorithms, implemented in Python. It includes detailed explanations and code examples for each concept. The repository is designed for educational purposes to fulfill an assignment requirement.

For the part about applications [view here](applications.md)

## Group Members
| Name              | Student ID       | Topic Assigned      |
|-------------------|------------------|---------------------|
| Ariel Boutcher    | BSCCS/2025/40350 | Heap Sort           |
| Fridah Harawo     | BSCCS/2025/35619 | Arrays              |
| Grace Wanjiru     | BSCCS/2025/39629 | Trees               |
| Loise Wambui      | BSCCS/2025/40219 | Queues              |
| Derrick Mburu     | BSCCS/2025/40404 | Quick Sort          |
| Benie Macharia    | BSCCS/2025/39532 | Binary Search trees |
| Rose Mateta       | BSCCS/2025/39761 | Stacks              |
| Ericson Karanja   | BSCCS/2025/39563 | Graphs              |
| Tinaelis Mumbi    | BSCCS/2025/40091 | Linked List         |

## Getting Started
To download and test the code, clone this repository:
```
git clone https://github.com/arpeli/dsa.git
```
Ensure you have Python installed to run the examples.

Please do not push code directly to the main branch. Create a separate branch and a pull request to request a merge.


### 1. Heap Sort – Ariel Boutcher

**What is it?**  
Heap sort is a way to sort numbers (or anything comparable) by first turning the list into a special structure called a **max-heap** — a complete binary tree where every parent is bigger than (or equal to) its children. Then we repeatedly take the biggest item out (the root) and put it at the end of the list.

**Why use it?**  
- Guaranteed O(n log n) time and therefore, never gets horribly slow like some other sorts  
- Doesn't need extra memory (in-place)  
- Good when you want predictable performance, like sorting large datasets without surprises

**How it works step by step**  
1. **Build the max-heap**: Imagine the array as a binary tree. Start from the middle of the array (the last non-leaf node) and work backwards to the root. For each node, check if it's bigger than its kids — if not, swap and keep checking downward (this is heapify).  
2. **Sort phase**: The biggest item is now at index 0. Swap it with the last unsorted item. Now the sorted part grows from the right.  
3. **Fix the heap**: The new root might be too small now, so we "heapify" downward from the top to restore the max-heap property — but only on the unsorted part.  
4. Repeat step 2–3 until everything is sorted. At the end, the array is sorted from smallest to largest.

**Time complexity**  
- Building heap: O(n) — surprisingly linear, not O(n log n)  
- Sorting: O(n log n) — from the repeated heapifies  
→ Overall: O(n log n) in worst, average, and best cases  
**Space complexity**: O(1) — no extra space needed

```python
def heapify(arr, n, i):
    # We assume the node at i might break the max-heap rule
    largest = i           # Start by thinking current node is biggest
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # If left child exists and is actually bigger → it wins
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Same check for right child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If we found a bigger child, swap and keep fixing that subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively fix the child we swapped with
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Phase 1: Build max-heap
    # We start from the last parent node (n//2 - 1) and go up to root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract max repeatedly
    for i in range(n - 1, 0, -1):
        # Swap root (biggest) with the last unsorted position
        arr[0], arr[i] = arr[i], arr[0]
        # Now heapify only the first i elements (heap size reduced)
        heapify(arr, i, 0)

    return arr

# Example
numbers = [38, 27, 43, 3, 9, 82, 10]
print("Before:", numbers)
heap_sort(numbers)
print("After heap sort:", numbers)
# Output: [3, 9, 10, 27, 38, 43, 82] — now sorted ascending
```

### 2. Arrays – Fridah Harawo

**What is it?**  
An array is a collection of items stored in **consecutive memory locations**. You can find any item instantly if you know its position (index). It's like a row of lockers — each has a number, and you can jump straight to locker 5.

**In Python**  
We use `list` — it's actually a **dynamic array** (it grows automatically when full, by doubling its size behind the scenes).

**Why useful?**  
- Super fast to read/write by index → O(1)  
- Used everywhere: storing scores, names, pixels in images, or even as building blocks for other structures like stacks  
- Simple and efficient for fixed-size data

**How it works step by step**  
1. **Create**: Just make a list with items.  
2. **Access**: Use index like arr[0] — first item. Indexes start at 0.  
3. **Add at end**: append() — usually fast, but sometimes resizes the whole array.  
4. **Insert in middle**: insert() — has to shift all later items right, so slow for big arrays.  
5. **Remove**: pop() or remove() — similar shifting if not at the end.  
6. **Search**: Loop through to find something — O(n) time.

**Time complexity**  
- Access: O(1)  
- Append: O(1) amortized  
- Insert/Delete middle: O(n)

**Space complexity**: O(n) for n items

```python
# Using Python list as an array
attendance = [True, False, True, True, False]  # Like a fixed row of values

# Access – instant, no matter how big the list
print("Person 3 attended?", attendance[2])     # True (index 2 is the third item)

# Add at end – usually fast (amortized O(1))
attendance.append(True)                        # Now has 6 items

# Insert in middle – slow, shifts everything right
attendance.insert(1, True)                     # Insert True at index 1
# Now: [True, True, False, True, True, False, True]

# Remove from middle – also slow, shifts left
attendance.pop(3)                              # Removes item at index 3 (True)

# Search for something – have to loop (O(n))
found = False in attendance                    # True

print("Final list:", attendance)
# Output: [True, True, False, True, False, True]
```

### 3. Queue – Loise Wambui

**What is it?**  
A queue is like a real-life line: **First person in is first person served** (FIFO = First In, First Out). You add (enqueue) at the back, remove (dequeue) from the front.

**Real-life examples**  
- Printer queue: Jobs wait in order  
- Waiting list for tickets or customer service  
- Task scheduling in apps or operating systems (e.g., background tasks)

**Why useful?**  
- Keeps things fair and ordered  
- Basis for algorithms like BFS (breadth-first search) in graphs

**How it works step by step**  
1. **Initialize**: Start with an empty list or deque.  
2. **Enqueue**: Add item to the end.  
3. **Dequeue**: Remove from the front and return it.  
4. **Peek**: Just look at the front without removing.  
5. **Check empty**: See if there's anyone left.  
If using a list, dequeue is slow (O(n) shift), so use deque for O(1) on both ends.

**Time complexity**  
- Enqueue/Dequeue: O(1) with deque  
- Peek: O(1)

**Space complexity**: O(n) for n items

```python
from collections import deque  # Best for queues — fast on both ends

class SimpleQueue:
    def __init__(self):
        # deque is perfect for queues
        self.queue = deque()

    def enqueue(self, customer):
        # Add to the back of the line
        self.queue.append(customer)
        print(f"{customer} joined the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty — no one to serve!")
            return None
        # Serve the person at the front
        served = self.queue.popleft()
        print(f"Serving {served}")
        return served

    def peek(self):
        if self.is_empty():
            return "No one in line"
        # Just look at the front
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

# Demo
bank_queue = SimpleQueue()
bank_queue.enqueue("Grace")    # Grace joined the queue
bank_queue.enqueue("Derrick")  # Derrick joined the queue
bank_queue.enqueue("Rose")     # Rose joined the queue

print("Next customer:", bank_queue.peek())     # Grace
bank_queue.dequeue()                            # Serving Grace
print("Now next is:", bank_queue.peek())       # Derrick
# Queue now: ['Derrick', 'Rose']
```

### 4. Tree – Grace Wanjiru

**What is it?**  
A tree is a hierarchical structure like a family tree or company org chart: one **root** at the top, then branches (children) below. No cycles — you can't loop back. We're focusing on **binary trees** (each node has at most 2 children).

**Real-life examples**  
- File systems: Folders inside folders  
- HTML DOM: Web page structure  
- Decision trees in AI

**Why useful?**  
- Great for hierarchies and quick searches (if balanced)  
- Basis for more advanced stuff like BSTs or heaps

**How it works step by step**  
1. **Nodes**: Each has data and pointers to children (left/right for binary).  
2. **Build**: Start with root, add children recursively.  
3. **Traversal**: Visit nodes in order. In-order: left subtree → root → right (gives sorted if BST).  
4. **Other traversals**: Pre-order (root first), post-order (root last).  
5. **Search/Insert**: Traverse down based on rules (e.g., left for smaller).

**Time complexity**  
- Traversal: O(n)  
- Search/Insert (balanced): O(log n), worst (skewed): O(n)

**Space complexity**: O(n)

```python
class Node:
    def __init__(self, value):
        self.value = value     # The data stored here
        self.left = None       # Pointer to left child
        self.right = None      # Pointer to right child

def in_order(node):
    if node:                   # If node exists
        in_order(node.left)    # Visit left subtree first
        print(node.value, end=" ")  # Then print root
        in_order(node.right)   # Then right subtree

# Manual build step by step
root = Node(50)                # Root at top
root.left = Node(30)           # Add left child
root.right = Node(70)          # Add right child
root.left.left = Node(20)      # Add to left of 30
root.left.right = Node(40)     # Add to right of 30

print("In-order traversal (left-root-right):")
in_order(root)
# Output: 20 30 40 50 70 — visits in sorted order for this tree
```

### 5. Quick Sort – Derrick Mburu

**What is it?**  
Quick sort is a **divide-and-conquer** algorithm: Pick a pivot, partition the array so smaller items are left and bigger right, then recursively sort both sides.

**Why use it?**  
- Very fast in practice: Average O(n log n)  
- In-place (little extra memory)  
- Used in many libraries (e.g., Python's sorted() sometimes uses it)

**How it works step by step**  
1. **Choose pivot**: Often the last item.  
2. **Partition**: Use two pointers — move smaller items left of pivot. At end, pivot is in correct position.  
3. **Recurse**: Quick sort left subarray (smaller than pivot) and right (bigger).  
4. **Base case**: If subarray has 0 or 1 item, it's sorted.  
Worst case (already sorted + bad pivot): O(n^2) — fix with random pivot.

**Time complexity**  
- Average/Best: O(n log n)  
- Worst: O(n^2)

**Space complexity**: O(log n) from recursion

```python
def partition(arr, low, high):
    pivot = arr[high]          # Pick last as pivot
    i = low - 1                # Pointer for smaller elements
    for j in range(low, high):
        if arr[j] <= pivot:    # If current is smaller/equal
            i += 1             # Move smaller pointer
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    # Place pivot in correct spot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1               # Return pivot's new index

def quick_sort(arr, low, high):
    if low < high:             # Base case: if not sorted yet
        pi = partition(arr, low, high)  # Partition and get index
        quick_sort(arr, low, pi - 1)    # Sort left
        quick_sort(arr, pi + 1, high)   # Sort right

# Example
marks = [64, 34, 25, 12, 22, 11, 90]
print("Before:", marks)
quick_sort(marks, 0, len(marks) - 1)
print("After quick sort:", marks)
# Output: [11, 12, 22, 25, 34, 64, 90]
```

### 6. Graphs – Ericson Karanja

**What is it?**  
A graph is nodes (vertices) connected by edges. Can be directed (one-way) or undirected, weighted (edges have costs) or not.

**Real-life examples**  
- Social networks: People as nodes, friendships as edges  
- Maps: Cities as nodes, roads as edges  
- Web: Pages as nodes, links as edges

**Why useful?**  
- Model relationships  
- Algorithms like shortest path (Dijkstra), search (BFS/DFS)

**How it works step by step**  
1. **Represent**: Adjacency list (dict of lists) — efficient.  
2. **Add edges**: Update the lists for both nodes if undirected.  
3. **Traverse**: BFS uses queue for levels; DFS uses stack/recursion for depth.  
4. **Search**: Start from a node, visit neighbors, mark visited to avoid cycles.

**Time complexity**  
- Add edge: O(1)  
- BFS/DFS: O(V + E) where V=nodes, E=edges

**Space complexity**: O(V + E)

```python
from collections import defaultdict, deque  # defaultdict for easy lists, deque for queue

class Graph:
    def __init__(self):
        # Adjacency list: key=node, value=list of neighbors
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add connection u → v
        self.graph[u].append(v)
        # And v → u for undirected
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()        # Track visited to avoid revisiting
        queue = deque([start]) # Queue for BFS
        visited.add(start)     # Mark start as visited

        while queue:
            node = queue.popleft()  # Get front of queue
            print(node, end=" ")    # Process (here: print)
            for neighbor in self.graph[node]:  # Check neighbors
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)  # Add to back

# Demo
g = Graph()
g.add_edge(0, 1)  # Connect 0-1
g.add_edge(0, 2)  # 0-2
g.add_edge(1, 2)  # 1-2
g.add_edge(2, 3)  # 2-3

print("BFS from 0:")
g.bfs(0)
# Output: 0 1 2 3 — visits level by level
```

### 7. Linked List – Tinaelis Mumbi

**What is it?**  
A linked list is nodes where each has data and a pointer to the next. No fixed size — grows dynamically. Singly linked: one-way pointers.

**Real-life examples**  
- Music playlist: Next song pointer  
- Undo in editors: Chain of states  
- Hash tables: Buckets as lists

**Why useful?**  
- Easy inserts/deletes anywhere (O(1) if you have the spot)  
- No wasted memory like arrays

**How it works step by step**  
1. **Nodes**: Data + next pointer.  
2. **Initialize**: Head points to first node.  
3. **Append**: Traverse to end, add new node.  
4. **Insert**: Find spot, update pointers.  
5. **Delete**: Find node, skip it by updating previous next.  
6. **Traverse**: Follow next from head.

**Time complexity**  
- Append: O(n) (traverse)  
- Insert/Delete: O(n) to find, then O(1)  
- Access: O(n) — no direct index

**Space complexity**: O(n)

```python
class Node:
    def __init__(self, data):
        self.data = data       # Store value
        self.next = None       # Pointer to next

class LinkedList:
    def __init__(self):
        self.head = None       # Start empty

    def append(self, data):
        new_node = Node(data)  # Create new
        if not self.head:      # If empty
            self.head = new_node
            return
        last = self.head       # Traverse to end
        while last.next:
            last = last.next
        last.next = new_node   # Link to new

    def print_list(self):
        current = self.head    # Start at head
        while current:
            print(current.data, end=" → ")
            current = current.next  # Move next
        print("None")          # End of list

# Demo
ll = LinkedList()
ll.append(10)  # Add 10
ll.append(20)  # Add 20
ll.append(30)  # Add 30
ll.print_list()
# Output: 10 → 20 → 30 → None
```

### 8. Stack – Rose Mateta

**What is it?**  
A stack is like a pile of plates: **Last In, First Out** (LIFO). Add (push) to top, remove (pop) from top.

**Real-life examples**  
- Browser back button: Page history  
- Function calls: Call stack in programs  
- Undo in apps

**Why useful?**  
- Simple for temporary storage  
- Basis for DFS, recursion

**How it works step by step**  
1. **Initialize**: Empty list.  
2. **Push**: Append to end (top).  
3. **Pop**: Remove last item.  
4. **Peek**: Look at last without removing.  
5. **Empty check**: Len == 0.

**Time complexity**  
- Push/Pop/Peek: O(1)

**Space complexity**: O(n)

```python
class Stack:
    def __init__(self):
        self.items = []        # Use list as stack

    def push(self, item):
        self.items.append(item)  # Add to top

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove top
        raise IndexError("Stack empty!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]    # Look at top
        raise IndexError("Stack empty!")

    def is_empty(self):
        return len(self.items) == 0

# Demo
s = Stack()
s.push("Book 1")  # Bottom
s.push("Book 2")  # Middle
s.push("Book 3")  # Top
print(s.pop())     # Book 3 (last in)
print(s.peek())    # Book 2 (now top)
# Stack now: ['Book 1', 'Book 2']
```

### 9. Binary Search Trees – Benie Macharia

**What is it?**  
A BST is a binary tree where left children < parent < right children. Keeps data sorted for fast lookups.

**Real-life examples**  
- Databases: Indexing for quick searches  
- Autocomplete: Sorted words  
- File search

**Why useful?**  
- Fast search/insert/delete: O(log n) if balanced  
- In-order traversal gives sorted list

**How it works step by step**  
1. **Insert**: Start at root, go left if smaller, right if bigger. Add when a spot is found.  
2. **Search**: Similar — traverse left/right until found or None.  
3. **Traversal**: In-order for sorted.  
4. **Delete**: Trickier — find, then handle cases (no child, one, two).  
Keeps balanced if inserts random; else can skew.

**Time complexity**  
- Search/Insert: O(log n) average, O(n) worst  
- Traversal: O(n)

**Space complexity**: O(n)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)  # First node
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:     # Go left
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:                      # Go right
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

# Demo
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
print("In-order (sorted):")
bst.in_order(bst.root)
# Output: 20 30 40 50 70
``` 
 
 
