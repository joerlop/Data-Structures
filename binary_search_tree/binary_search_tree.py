import sys
sys.path.append('../queue_and_stack')
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
  def __init__(self, value): # We're just using value, so key is value
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
    pass

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass