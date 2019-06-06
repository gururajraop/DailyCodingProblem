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


def count_univalued_subtree(Tree):
    pass


if __name__ == '__main__':
    Tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    str = "Space:" + '' * 0 + ":"
    print("Given input tree is:")
    print_tree(Tree)
    result = count_univalued_subtree(Tree)
    print("\n\nNumber of univalued subtrees: ", result)