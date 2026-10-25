# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment covered two data structures: stacks (LIFO) and queues (FIFO).

## What I Did

- Created a stack using a Python list.
- Created a queue using `collections.deque`.
- Added methods to add, remove, and view items.
- Tested how each structure handled items in different orders.
- Tested what happened when removing or viewing items from an empty structure.
- Tested adding and removing a single item.

## How They Work

**Stack:** The stack followed LIFO, meaning the last item added was the first one removed. This was demonstrated by adding actions and removing them in reverse order.

**Queue:** The queue followed FIFO, meaning the first item added was the first one removed. This was demonstrated with a line of customers being served in order.

## Testing

I tested both structures with four items, empty structures, and single-item examples. The program displayed messages when I tried to remove or view items from an empty structure. I also checked that each structure was empty after its only item was removed.

## Real-World Examples

A stack can be used for the undo feature in a text editor. A queue can be used for customers waiting in line at a coffee shop.