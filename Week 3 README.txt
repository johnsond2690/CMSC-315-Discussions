# Unit 3 Discussion: List Operations

## Overview

This assignment demonstrated how Python lists handled insertion, deletion, and searching. The program used built-in list operations and a linear search function to show how list elements changed during different operations.

## Learning Objectives

- Inserted values at the beginning, middle, and end of a list.
- Deleted values from different list positions.
- Searched for existing and missing values.
- Tested edge cases involving empty lists and invalid indexes.
- Examined how list operations affected performance.

## Implementation

The program included three main functions:

- **insert_at():** Used Python's `insert()` method to add values at specified indexes. Existing elements shifted to make room for new values.
- **delete_at():** Validated the requested index and used `pop()` to remove and return the selected value. Invalid indexes returned `None`.
- **search_value():** Used a linear search to check each element sequentially. It returned the matching index or `-1` when the value was not found.

## Testing

The program demonstrated insertion and deletion at the beginning, middle, and end of a list. It also tested searches for existing and missing values. Additional edge cases included inserting into an empty list, deleting from an empty list, and attempting deletion with an invalid index.

## Real-World Scenario

An inventory example demonstrated how a list could be used to manage products. The program added a monitor, searched for a mouse, and removed a laptop from the inventory.

## Performance Observations

Insertion and deletion near the beginning or middle of a Python list required existing elements to shift. Operations at the end generally required less work. Searching used a linear approach, meaning the program checked elements one at a time. This made searching less efficient as the list grew larger.

## Discussion Board Reflection

The assignment helped demonstrate how Python lists handled insertion, deletion, and searching. It also showed how the position of an element affected performance. I learned that inserting or deleting items near the beginning of a list required other elements to shift, while operations at the end were generally faster.

