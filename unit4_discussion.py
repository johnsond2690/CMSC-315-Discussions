
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Store the value assigned to this node.
        self.value = value

        # Initialize both child references as None.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # The root is None until the first value is inserted.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start the recursive insertion at the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # Base case: create a new node when an empty position is found.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        # This maintains the BST ordering property.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored to avoid duplicate entries.

        # Return the current node after updating its child.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # Begin searching from the root node.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Base case: an empty node means the value was not found.
        if node is None:
            return False

        # Return True if the current node matches the target.
        if node.value == value:
            return True

        # Search the left subtree if the target is smaller.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, search the right subtree.
        return self._search_recursive(node.right, value)

        # BST searching can eliminate one subtree at each step.
        # A balanced tree takes approximately O(log n) time,
        # while a linear search takes O(n) time.

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        # Create a list to store the traversal results.
        values = []

        # Start the recursive traversal at the root.
        self._inorder_recursive(self.root, values)

        # Return the completed list.
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Base case: stop when an empty node is reached.
        if node is None:
            return

        # First, visit all nodes in the left subtree.
        self._inorder_recursive(node.left, values)

        # Next, add the current node's value.
        values.append(node.value)

        # Finally, visit all nodes in the right subtree.
        self._inorder_recursive(node.right, values)

        # In-order traversal produces ascending values because
        # smaller values are stored on the left and larger
        # values are stored on the right.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create a Binary Search Tree.
    employee_tree = BST()

    # Employee ID numbers inserted in a balanced order.
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]

    # Insert each employee ID into the tree.
    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)

    # A BST reduces the search space by comparing values
    # and selecting only the left or right subtree.
    # Starting with a middle value helps create a balanced tree.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Display employee IDs in ascending order.
    sorted_ids = employee_tree.inorder()

    print("Sorted employee IDs:", sorted_ids)

    # In-order traversal visits the left subtree,
    # then the current node, and finally the right subtree.
    # This produces sorted output in a BST.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for employee IDs that exist.
    print("Searching for employee 1025:",
          employee_tree.search(1025))

    print("Searching for employee 1090:",
          employee_tree.search(1090))

    # Search for employee IDs that do not exist.
    print("Searching for employee 1000:",
          employee_tree.search(1000))

    print("Searching for employee 1100:",
          employee_tree.search(1100))

    # Existing employee IDs return True.
    # Missing employee IDs return False.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Test an empty tree.
    empty_tree = BST()

    print("Empty tree traversal:", empty_tree.inorder())
    print("Search empty tree:", empty_tree.search(1050))

    # Test inserting a duplicate value.
    employee_tree.insert(1025)

    print("After inserting duplicate 1025:",
          employee_tree.inorder())

    # Test a tree containing only one node.
    single_tree = BST()
    single_tree.insert(5000)

    print("Single-node tree:", single_tree.inorder())
    print("Search for 5000:", single_tree.search(5000))
    print("Search for 6000:", single_tree.search(6000))

    # These tests demonstrate that the BST handles empty trees,
    # duplicate values, and single-node trees without errors.


if __name__ == "__main__":
    main()
