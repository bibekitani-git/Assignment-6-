class Stack:
    """A LIFO Stack implementation using a Python list."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Returns True if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Adds an item to the top of the stack. O(1) amortized."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top. O(1)."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the top item without removing it. O(1)."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)
