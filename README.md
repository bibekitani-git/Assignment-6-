# Assignment-6-
Medians and Order Statistics &amp; Elementary Data Structures

This repository contains the Python code and analysis report for "Assignment 6: Medians and Order Statistics & Elementary Data Structures."

## Repository Structure

- `report.pdf`: The full analysis report (this document).
- `RandomizedQS.py` and `DeterministicSelectMOM.py`: Contains the Python code for Randomized Quickselect and Deterministic (Median of Medians) Select.
- `Stack.py` , `Queue.py`,  and `LinkedList.py` : Contains the Python class implementations for Stack, Queue, and Singly Linked List.
- `README.md`: This file.

## How to Run the Code

The Python files (`.py`) are libraries containing the implemented algorithms and data structures. They are designed to be imported into other scripts for use.

### Example Usage:

You can import these classes and functions into your own test script.

**Testing Selection Algorithms:**

```python
# test_selection.py
from selection_algorithms import randomized_quickselect, deterministic_select

my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 4  # Find the 4th smallest element (0-based index)

# Note: The algorithms may modify the array in-place
arr_copy1 = list(my_array)
arr_copy2 = list(my_array)

# The sorted version is [1, 1, 2, 3, 4, 5, 5, 6, 9]
# The 4th index (5th smallest) is 4
result_random = randomized_quickselect(arr_copy1, 0, len(arr_copy1) - 1, k)
result_det = deterministic_select(arr_copy2, 0, len(arr_copy2) - 1, k)

print(f"Original array: {my_array}")
print(f"The {k}-th smallest element (Randomized): {result_random}")
print(f"The {k}-th smallest element (Deterministic): {result_det}")
