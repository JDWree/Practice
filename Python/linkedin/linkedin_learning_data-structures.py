# Stacks, queues and deques - data types

# Stacks: an abstact data type that stores items in the order
#           in which they were added.
#           Items are added to and removed from the "top" of a Stacks
#           aka: LIFO (last in first out)
#           In python: we could use a list.
# Example: linter in text editors, reversing characters of a string
# Stacks work recursive.

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of our list.
        It returns nothing.

        Runtime: O(1) constant time. (indexing = O(1))
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item from the list = top item from the stack.

        Runtime: O(1) = constant time (indexing to last item of the list)"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the last item in the list = top item in the stack.

        Runtime: O(1)"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list (stack).

        Runtime: O(1)"""
        return len(self.items)

    def is_empty(self):
        """Returns bool whether list (stack) is empty or not.

        Runtime: O(1)"""
        if len(self.items) == 0:
            return True
        return False

def linter(string):
    """Checks whether a string has matching opening and closing brackets."""
    stack = Stack()
    opening = ("(","[","{")
    closing = (")","]","}")

    for s in string:
        if s in opening:
            stack.push(s) # Put an opening bracket in the stack.
        elif s in closing:
            # Check if top item of stack equals the matching opening bracket.
            # While popping the top item of the stack.
            # Return false if they don't match.
            if opening[closing.index(s)] != stack.pop():
                return False
    # Should be empty if all brackets were correctly matched.
    # This also returns true if string was empty or didn't contain brackets.
    return stack.is_empty()

# linter("()[]()")    # --> should return True
# linter("[]][")      # --> should return False
# linter("")          # --> True
# linter("Abc")       # --> True
# linter("(a*[b+c])/d") # --> True
# linter("){}")       # --> False
# linter("[](")       # --> False
# linter("((())")     # --> False
################################################################################

# Queues: abstact data type where items stored are saved in the order they were stored.
#           Items are added in the back and removed from the front.
#           (First in, first out: FIFO)
# Examples: printer queue
# Queues is a recursive data structure (empty or first item and rest also a queue)

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the back of the queue (= front of the list!)
                    --> insert to the 0th index in the list.
        Runtime: O(n) linear time: the bigger the queue, the longer it takes to add another item.
        """
        self.items.insert(0, item)


    def dequeue(self):
        """Returns and removes the front item of the queue (= last item of the list).

        Runtime: O(1) constant: does not depend on the size of the queue."""
        if self.items:
            return self.items.pop()
        return None


    def peek(self):
        """Returns the first item of the queue.
        Returns None if empty

        Runtime: O(1)"""
        if self.items:
            return self.items[-1]
        return None


    def size(self):
        return len(self.items)


    def is_empty(self):
        return self.items == []

###############################################################################

# Deque: Double-Ended QUEue
#       An abstarct data type that resembles both a stack and a queue.
#       Items in a deque can be added to and removed from both the back and front.
#       They are sort of sorted?
#       Both FIFO and LIFO
# Examples: checking if string is palindrome

class Deque:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        """Inserts an item in the 0th index of the list = first item of the deck.
        Runtime: O(n), linear
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """Adds an item to the back of the list/deque.
        Runtime: O(1), constant
        """
        self.items.append(item)

    def remove_front(self):
        """Returns and removes the item from the front of the list.
        Runtime: O(n), linear
        """
        return self.items.pop(0)

    def remove_rear(self):
        """Returns and removes the last item from the list.
        Runtime: O(1), constant
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """Returns the first item of the list."""
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """Returns the last item of the list."""
        if self.items:
            return self.items[-1]
        return None

import numpy as np

def palindrome_check(string):
    deque = Deque()
    for c in string:
        deque.add_rear(c.lower()) # add_rear faster than add_front

    #for i in range(int(np.floor(deque.size()/2))):
    while deque.size() >= 2:
        if deque.remove_rear() != deque.remove_front():
            return False
    return True
