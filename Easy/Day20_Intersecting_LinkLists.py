"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

import os
import sys
import numpy as np


class node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_item(self, item):
        if self.head is None:
            self.head = node(val=item)
            self.tail = self.head
        else:
            Node = node(val=item)
            self.tail.next = Node
            self.tail = self.tail.next
        self.size += 1

    def print_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.value)
            current = current.next

        print(items)

    def __len__(self):
        return self.size


def create_linked_list(lst):
    root = Linked_List()
    for item in lst:
        root.add_item(item)

    return root


def find_intersection(list1, list2):
    return -1


if __name__ == '__main__':
    M = np.random.randint(low=5, high=15, size=1)[0]
    list1 = np.random.randint(low=1, high=50, size=M)
    list1 = create_linked_list(list1)
    print("Items in the list-1 are: ")
    list1.print_list()

    N = np.random.randint(low=5, high=15, size=1)[0]
    list2 = np.random.randint(low=1, high=50, size=N)
    list2 = create_linked_list(list2)
    print("Items in the list-2 are: ")
    list2.print_list()

    intersection = find_intersection(list1, list2)
    if intersection == -1:
        print("\nThe lists do not intersect")
    else:
        print("\n The lists intersect at node: ", intersection)