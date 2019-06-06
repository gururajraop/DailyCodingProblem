"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
           0
          / \
         1   0
            / \
           1   0
          / \
         1   1
"""

import os
import sys
import numpy as np


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(root, space=0):
    if root is not None:
        print(root.value, end = '')
        if root.left is not None:
            print("__", end = '')
            print_tree(root.left, space+1)
        if root.right is not None:
            extra = "\n" + '   ' * space + "|__"
            print(extra, end='')
            print_tree(root.right, space+1)


def check_univalued_tree(root, value):
    if root.value != value:
        return False

    if root.left is not None:
        univalued_tree = check_univalued_tree(root.left, value)
        if not univalued_tree:
            return False
    if root.right is not None:
        univalued_tree = check_univalued_tree(root.right, value)
        if not univalued_tree:
            return False

    return True


def count_univalued_subtree(root):
    if root is None:
        return 0

    # If leaf node return 1
    if (root.left is None) and (root.right is None):
        return 1

    count = 0
    same_children = True
    if root.left is not None:
        if not check_univalued_tree(root.left, root.value):
            same_children = False
        count += count_univalued_subtree(root.left)

    if root.right is not None:
        if not check_univalued_tree(root.right, root.value):
            same_children = False
        count += count_univalued_subtree(root.right)

    if same_children:
        count += 1

    return count


if __name__ == '__main__':
    Tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    str = "Space:" + '' * 0 + ":"
    print("Given input tree is:")
    print_tree(Tree)
    print("")
    result = count_univalued_subtree(Tree)
    print("Number of univalued subtrees: ", result)

    Tree = Node(1, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1)))
    str = "Space:" + '' * 0 + ":"
    print("\n\nGiven input tree is:")
    print_tree(Tree)
    print("")
    result = count_univalued_subtree(Tree)
    print("Number of univalued subtrees: ", result)