class Queue:
    """A FIFO Queue implementation using a Python list."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Returns True if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Adds an item to the back of the queue. O(1) amortized."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item from the front. O(n)."""
        if not self.is_empty():
            # pop(0) is inefficient, must shift all other elements
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Returns the front item without removing it. O(1)."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)
