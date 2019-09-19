from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints?
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    def insert(self, value):

        current = self
        done = False

        while done == False:

            if value < current.value:
                if current.left is None:
                    bst = BinarySearchTree(value)
                    current.left = bst
                    done = True
                else:
                    current = current.left

            else:
                if current.right is None:
                    bst = BinarySearchTree(value)
                    current.right = bst
                    done = True
                else:
                    current = current.right

    # * `contains` searches the binary search tree for the input value,
    # returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children
    def contains(self, target):

        current = self
        done = False

        while done == False:

            if current.value == target:
                return True

            elif current.left is None and current.right is None:
                return False

            elif target < current.value:
                current = current.left

            else:
                current = current.right

    # * `get_max` returns the maximum value in the binary search tree.

    def get_max(self):
        current = self
        done = False

        while done == False:

            if current.right is None:
                return current.value

            else:
                current = current.right

    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):

        current = self
        cb(current.value)

        if current.right:
            current.right.for_each(cb)

        if current.left:
            current.left.for_each(cb)

# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self, node):

        if node.left:
            node.left.in_order_dft(node.left)

        print(self.value)

        if node.right:
            node.right.in_order_dft(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Breadth first search - queue
        # check each level one at a time
        # create a queue
        node_queue = Queue()
        # put root in queue
        node_queue.enqueue(node)
        # while queue is not empty
        while node_queue.len() > 0:
            # pop first item in queue
            current_node = node_queue.dequeue()
            print(current_node.value)
        # check left and right add to queue
            if current_node.left:
                node_queue.enqueue(current_node.left)

            if current_node.right:
                node_queue.enqueue(current_node.right)
        # shift
        # go to head of queue and continue

   # Print the value of every node, starting with the given node,
   # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack
        node_stack = Stack()
        # put root in stack
        node_stack.push(node)
        # while stack is not empty
        while node_stack.len() > 0:
            # pop first item in stack
            current_node = node_stack.pop()
            print(current_node.value)
        # check root.left and put it in stack
            if current_node.left:
                node_stack.push(current_node.left)
        # check root.right and put it in stack
            if current_node.right:
                node_stack.push(current_node.right)
        # go to top of stack and continue

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
