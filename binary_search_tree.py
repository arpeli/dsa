# By Benie Macharia
# Binary Search Tree (BST) - O(log n) average case for search/insert/delete
# Left subtree < parent < right subtree
class Node:
    """Node with value and pointers to left and right children"""
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation"""
    def _init_(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST"""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """Helper method to recursively insert value"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        """Search for a value in the BST"""
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def in_order(self, node):
        """In-order traversal: left -> root -> right (gives sorted order)"""
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    def delete(self, value):
        """Delete a node from the BST"""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: get inorder successor
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_value_node(self, node):
        """Helper to find the smallest value in a subtree"""
        current = node
        while current.left:
            current = current.left
        return current

# Example usage
if _name_ == "_main_":
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("In-order (sorted):")
    bst.in_order(bst.root)
    print("\n")

    # Searching values
    print("Search 40:", bst.search(40))
    print("Search 90:", bst.search(90))

    # Deleting a value
    bst.delete(30)
    print("In-order after deleting 30:")
    bst.in_order(bst.root)
    print()

    