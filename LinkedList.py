class Node:
    """A node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_front(self, data):
        """Inserts a new node at the beginning. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end. O(n)."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        """Deletes the first node found with the given key. O(n)."""
        current = self.head
        
        # If head node holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
            
        if current is None:
            print("Key not found in list")
            return
            
        # Unlink the node
        prev.next = current.next
        current = None

    def traverse(self):
        """Prints all elements in the list. O(n)."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
