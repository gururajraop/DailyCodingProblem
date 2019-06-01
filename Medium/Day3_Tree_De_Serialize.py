"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import os
import sys
import numpy as np


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    string = root.val
    if (root.left is not None) and (root.right is not None):
        string = string + ' ' + serialize(root.left) + ' ' + serialize(root.right)
    elif root.left is not None:
        string = string + ' ' + serialize(root.left) + ' None'
    else:
        string = string + ' None None'

    return string


def get_left_node(s, idx):
    if s[0] == 'None':
        return None, idx
    left_node, idx = get_left_node(s[1:], idx+1)
    right_node, idx = get_right_node(s[idx:], idx)
    node = Node(s[0], left=left_node, right=right_node)

    return node, idx+1


def get_right_node(s, idx):
    if len(s) == 1:
        return Node(s[0], left=None, right=None), idx+1

    if s[0] == 'None':
        return None, idx+1

    left_node, idx = get_left_node(s[1:], idx+1)
    right_node, idx = get_right_node(s[idx:], idx)
    node = Node(s[0], left=left_node, right=right_node)

    return node, idx


def deserialize(s):
    s_list = s.split() if isinstance(s, str) else s
    if len(s_list) == 1:
        return Node(s_list[0])
    else:
        left_node, idx = get_left_node(s_list[1:], 0)
        right_node, idx = get_right_node(s_list[idx:], 0)
        node = Node(s_list[0], left=left_node, right=right_node)
        return node


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    print("PASS")