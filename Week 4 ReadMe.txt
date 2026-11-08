# Unit 4 Discussion: Binary Search Trees

## Overview

I used a BST in Python using employee ID numbers to demonstrate how data can be organized and searched efficiently.

## Learning Objectives

- Build a Binary Search Tree.
- Insert values recursively.
- Search recursively.
- Perform in-order traversal.
- Understand how BSTs organize data.

## Implementation

I created a `Node` class to store each employee ID and references to its left and right child nodes. I also created a `BST` class to manage the tree.

The program included the following functionality:

1. Created an empty Binary Search Tree.
2. Inserted multiple employee ID numbers using recursive insertion.
3. Placed smaller values in the left subtree and larger values in the right subtree.
4. Implemented recursive searching to locate employee IDs.
5. Used in-order traversal to display employee IDs in ascending order.
6. Tested searches for existing and missing values.
7. Tested edge cases involving empty trees, duplicate values, and single-node trees.

Duplicate values were ignored to prevent unnecessary duplicate entries.

## Testing and Expected Results

The program was tested using the following employee ID numbers:

`1050, 1025, 1075, 1010, 1035, 1060, 1090`

The expected in-order traversal was:

`[1010, 1025, 1035, 1050, 1060, 1075, 1090]`

Search tests included employee IDs that existed in the tree and IDs that were not present. Additional tests verified that searching an empty tree returned false, duplicate values were not added, and a tree containing only one node functioned correctly.

## Conclusion

This assignment demonstrated how Binary Search Trees can be used to organize employee records and retrieve information efficiently. The implementation reinforced recursive programming, searching, insertion, and tree traversal.