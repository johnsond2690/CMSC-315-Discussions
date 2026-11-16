
# Unit 5 Discussion: Search Algorithms

## Overview

For this assignment, I worked with two different search methods in Python: linear search and binary search. I tested both methods using small and large lists to see how they performed and how they handled different situations.

## What I Worked On

### Linear Search

I created a function that checked each item in a list until it found the number I was looking for. If the number was not in the list, the function returned -1.

Linear search has O(n) time complexity because it may need to go through the entire list.

### Binary Search

I also created a binary search function. Instead of checking every item, it looked at the middle of the list and narrowed down the search based on the result.

This process continued until the number was found or there were no more items to check.

Binary search has O(log n) time complexity. One thing I had to account for was that the list needed to be sorted before using this method.

## Testing

### Small List

I started with a list containing seven numbers. I tested both methods with a number that was in the list and another number that was not.

Both methods returned the correct results.

### Large List

Next, I created a list containing 10,000 numbers and searched for 75,000.

Both methods found the number at index 7,500. This test helped show why binary search is more useful when working with larger lists.

### Edge Cases

I tested a few situations that could cause problems:

- Empty list: Both methods returned -1.
- Single-item list: Both methods found the number when it was present.
- Missing number: Both methods returned -1.
- First and last positions: Binary search found values at both ends of the list.

All of these tests worked as expected.

## Real-World Example

I used employee ID numbers as an example. The program searched through a list of employee IDs to find a specific employee.

Since the IDs were already sorted, binary search was a good choice. If the list was not organized, linear search would still work without having to sort everything first.

## What I Learned

This assignment helped me understand the difference between the two search methods. Linear search is simple and works with unsorted data, but it can take longer when the list gets bigger. Binary search is much faster with larger lists, but the data has to be sorted first.

Overall, I learned that the best search method depends on how the information is organized and how much data needs to be searched.
