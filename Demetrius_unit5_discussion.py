
"""
Unit 5 Discussion: Search Algorithms

This program shows how linear search and binary search work.
It tests both methods with different lists and compares
how they handle different search situations.
"""


def linear_search(lst, target):
    """
    Checks each item in the list until the target is found.
    Returns the position if found, or -1 if it is not there.
    """

    # Start at the beginning and check each item.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 if the loop finishes without finding the value.
    return -1

    # Linear search is O(n) because it may have to check
    # every item in the list.


def binary_search(lst, target):
    """
    Searches through a sorted list by checking the middle value.
    Each time, it cuts the search area in half.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find the middle position of the current search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            # The target is larger, so look at the right side.
            left = middle + 1

        else:
            # The target is smaller, so look at the left side.
            right = middle - 1

    # Return -1 if the target is not in the list.
    return -1

    # Binary search is O(log n) because it removes
    # about half of the remaining values each time.


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # A small list of numbers to test both methods.
    small_dataset = [5, 10, 15, 20, 25, 30, 35]

    # Test a number that is in the list.
    target = 20

    print("List:", small_dataset)
    print("Searching for:", target)
    print("Linear search result:", linear_search(small_dataset, target))
    print("Binary search result:", binary_search(small_dataset, target))

    # Test a number that is not in the list.
    target = 100

    print("\nSearching for a number that is not in the list:", target)
    print("Linear search result:", linear_search(small_dataset, target))
    print("Binary search result:", binary_search(small_dataset, target))

    # Both methods should return -1 when the number is missing.

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create a list with 10,000 sorted numbers.
    large_dataset = list(range(0, 100000, 10))

    target = 75000

    print("Number of items in list:", len(large_dataset))
    print("Searching for:", target)
    print("Linear search result:", linear_search(large_dataset, target))
    print("Binary search result:", binary_search(large_dataset, target))

    # Both methods find the same position.
    # Binary search is more efficient with a large sorted list
    # because it does not have to check every number.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Test 1: An empty list.
    empty_list = []

    print("\nTesting an empty list:")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # There are no items to search, so both return -1.

    # Test 2: A list with only one item.
    single_list = [25]

    print("\nTesting a list with one item:")
    print("Searching for 25:")
    print("Linear search:", linear_search(single_list, 25))
    print("Binary search:", binary_search(single_list, 25))

    # Both methods find the value at index 0.

    # Test 3: A value that is not in the list.
    print("\nSearching for 50 in the single-item list:")
    print("Linear search:", linear_search(single_list, 50))
    print("Binary search:", binary_search(single_list, 50))

    # Test 4: Check the first and last items in a list.
    boundary_list = [10, 20, 30, 40, 50]

    print("\nTesting the first and last positions:")
    print("First item:", binary_search(boundary_list, 10))
    print("Last item:", binary_search(boundary_list, 50))

    # These tests make sure binary search handles both ends
    # of the list correctly.

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD SEARCH EXAMPLE ===")

    # Imagine looking for an employee using their ID number.
    employee_ids = [1001, 1005, 1010, 1015, 1020, 1025, 1030]

    employee_to_find = 1020

    print("Employee IDs:", employee_ids)
    print("Looking for employee:", employee_to_find)
    print("Linear search:", linear_search(employee_ids, employee_to_find))
    print("Binary search:", binary_search(employee_ids, employee_to_find))

    # Since the employee IDs are already sorted, binary search
    # is a good option. If they were not sorted, linear search
    # could be used without having to organize them first.


if __name__ == "__main__":
    main()
