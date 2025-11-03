import random

def swap(arr, a, b):
    """Helper function to swap two elements in an array."""
    arr[a], arr[b] = arr[b], arr[a]

def randomized_partition(arr, left, right):
    """
    Picks a random pivot, partitions the array, and returns
    the pivot's final index.
    """
    # Choose a random pivot index
    pivot_index = random.randint(left, right)
    pivot_value = arr[pivot_index]
    
    # Move pivot to the end
    swap(arr, pivot_index, right)
    
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, store_index)
            store_index += 1
            
    # Move pivot to its final sorted position
    swap(arr, store_index, right)
    return store_index

def randomized_quickselect(arr, left, right, k):
    """
    Finds the k-th smallest element (k is 0-based) in an array
    using the randomized Quickselect algorithm.
    
    k is the 0-based index of the element we want, e.g., k=0 for the minimum.
    """
    if left == right:
        return arr[left]
        
    while left <= right:
        # Partition the array
        pivot_index = randomized_partition(arr, left, right)
        
        if pivot_index == k:
            # The pivot is the k-th smallest element
            return arr[pivot_index]
        elif k < pivot_index:
            # The k-th element is in the left partition
            right = pivot_index - 1
        else:
            # The k-th element is in the right partition
            left = pivot_index + 1
            
    return -1 # Should not be reached
