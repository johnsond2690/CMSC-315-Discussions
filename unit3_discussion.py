"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # The insert() method adds the new value at the requested position.
    # Existing elements at that position and after it shift one position right.
    # Inserting at the beginning or middle takes longer because more elements
    # may need to shift. Inserting at the end is generally faster.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check that the index is within the valid range before deleting.
    # This prevents errors and avoids attempting to remove an item that
    # does not exist. Negative indexes are valid in Python when in range.
    if -len(lst) <= index < len(lst):
        # pop() removes the item and returns its value.
        # Remaining elements shift left to fill the empty position.
        return lst.pop(index)

    # Return None when the index is invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because it checks each element one at a time.
    # The search moves sequentially through the list until it finds the value.
    # In the worst case, every element must be checked, making the time
    # complexity O(n).
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when the value is not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)

    # Insert at index 0, moving the existing elements to the right.
    insert_at(numbers, 0, 5)
    print("After inserting at the beginning:", numbers)

    # Insert at index 3, shifting the remaining elements to the right.
    insert_at(numbers, 3, 25)
    print("After inserting in the middle:", numbers)

    # Insert at the end of the list.
    insert_at(numbers, len(numbers), 60)
    print("After inserting at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first item. All remaining items shift left.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Remove an item from the middle of the updated list.
    removed = delete_at(numbers, 2)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Remove the last item.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a value that is in the list.
    result = search_value(numbers, 30)
    print("Searching for 30. Index found:", result)

    # Search for a value that is not in the list.
    result = search_value(numbers, 100)
    print("Searching for 100. Result (-1 means not found):", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Attempt to delete an item using an invalid index.
    removed = delete_at(numbers, 100)
    print("Attempt to delete using invalid index:", removed)

    # Insert into an empty list to demonstrate that insertion still works.
    empty_list = []
    insert_at(empty_list, 0, "First item")
    print("After inserting into an empty list:", empty_list)

    # Attempt to delete from an empty list.
    removed = delete_at(empty_list, 0)
    print("Attempt to delete from an empty list:", removed)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO: INVENTORY ===")

    # A list can be used to keep track of products in a small inventory.
    inventory = ["Laptop", "Keyboard", "Mouse"]
    print("Current inventory:", inventory)

    # Add a new product to the inventory.
    insert_at(inventory, 1, "Monitor")
    print("After adding a monitor:", inventory)

    # Search for a product.
    result = search_value(inventory, "Mouse")
    print("Mouse found at index:", result)

    # Remove a product from the inventory.
    removed = delete_at(inventory, 0)
    print("Removed product:", removed)
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
