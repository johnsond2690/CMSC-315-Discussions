
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding to the top means the newest item will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Cannot pop: the stack is empty."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return "Cannot peek: the stack is empty."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # New items join the back so earlier items are served first (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Cannot dequeue: the queue is empty."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Front lets us view the next item while keeping it in the queue.
        if self.is_empty():
            return "Cannot view front: the queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    # Create a stack and add four actions.
    action_stack = Stack()
    for action in ["Open file", "Edit text", "Save file", "Print file"]:
        action_stack.push(action)
        print(f"Added to stack: {action}")

    # Demonstrate LIFO: the last action added is removed first.
    print("\nRemoving actions in LIFO order:")
    while not action_stack.is_empty():
        print(f"Removed: {action_stack.pop()}")

    # Test popping and peeking at an empty stack.
    print("\nTesting empty-stack behavior:")
    print(action_stack.pop())
    print(action_stack.peek())

    # Test a stack containing only one item.
    print("\nTesting a single-item stack:")
    single_stack = Stack()
    single_stack.push("One action")
    print(f"Removed: {single_stack.pop()}")
    print(f"Is the stack empty? {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    # Create a queue of customers.
    customer_queue = Queue()
    for customer in ["Alex", "Jordan", "Taylor", "Morgan"]:
        customer_queue.enqueue(customer)
        print(f"Customer joined the queue: {customer}")

    # Demonstrate FIFO: the first customer added is served first.
    print("\nServing customers in FIFO order:")
    while not customer_queue.is_empty():
        print(f"Customer served: {customer_queue.dequeue()}")

    # Test dequeuing and viewing the front of an empty queue.
    print("\nTesting empty-queue behavior:")
    print(customer_queue.dequeue())
    print(customer_queue.front())

    # Test a queue containing only one item.
    print("\nTesting a single-item queue:")
    single_queue = Queue()
    single_queue.enqueue("Casey")
    print(f"Customer served: {single_queue.dequeue()}")
    print(f"Is the queue empty? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
