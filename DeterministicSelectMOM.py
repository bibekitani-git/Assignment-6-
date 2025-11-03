def find_median_of_five(sub_list):
    """Finds the median of a small list (<= 5 elements)."""
    return sorted(sub_list)[len(sub_list) // 2]

def deterministic_partition(arr, left, right, pivot_value):
    """
    Partitions the array around a specific pivot_value.
    Returns the final index of the pivot.
    """
    # Find the pivot value in the array and move it to the end
    pivot_index = -1
    for i in range(left, right + 1):
        if arr[i] == pivot_value:
            pivot_index = i
            break
    swap(arr, pivot_index, right)

    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, store_index)
            store_index += 1
            
    swap(arr, store_index, right)
    return store_index

def deterministic_select(arr, left, right, k):
    """
    Finds the k-th smallest element (k is 0-based) using the
    Median of Medians algorithm.
    """
    if left == right:
        return arr[left]

    while True:
        # 1. Divide the array into groups of 5
        medians = []
        for i in range(left, right + 1, 5):
            sub_list = arr[i : min(i + 5, right + 1)]
            median = find_median_of_five(sub_list)
            medians.append(median)
        
        # 2. Find the median of the medians recursively
        if len(medians) == 1:
            pivot = medians[0]
        else:
            # We use deterministic_select to find the median of medians
            # We need a copy because the function modifies the array
            medians_copy = list(medians)
            pivot = deterministic_select(medians_copy, 0, len(medians) - 1, len(medians) // 2)

        # 3. Partition the original array around the pivot
        pivot_index = deterministic_partition(arr, left, right, pivot)

        # 4. Check pivot position and recurse
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
