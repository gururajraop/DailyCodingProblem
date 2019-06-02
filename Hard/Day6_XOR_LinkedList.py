"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
"""

import os
import sys
import numpy as np


class Node():
    def __init__(self, value, both=0):
        self.value = value
        self.both = both


class XOR_LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_item(self):
        item = int(input("Please enter the item to be added to the list: "))
        node = Node(value=item)
        if self.head is None:
            assert (self.size == 0) and (self.tail is None), "Error!! Something wrong with the list"
            self.head = self.tail = node
            self.size += 1
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        print("Item {} added successfully to the list at position {}".format(item, self.size))

    def remove_item(self):
        pass

    def get_item(self):
        pass

    def print_items(self):
        pass

    def __len__(self):
        return self.size


def print_options():
    print("----------------------Linked list options----------------------")
    print("\t1:\tInsert an item to the list")
    print("\t2:\tDelete an item from the list")
    print("\t3:\tGet an item from the list at given index")
    print("\t4:\tPrint the elements of the list")
    print("\t5:\tPrint the options menu")
    print("\t0:\tExit")
    print("------------------------------End------------------------------")


def err_message():
    print("Invalid option entered")


def switch(obj, options):
    switcher = {
        0: -1,
        1: obj.add_item,
        2: obj.remove_item,
        3: obj.get_item,
        4: obj.print_items,
        5: print_options
    }
    return switcher.get(options, err_message())

if __name__ == '__main__':
    print_options()
    link_list = XOR_LinkedList()
    option = 1

    while option != 0:
        option = int(input("----->Please enter your option: "))
        func = switch(link_list, option)
        if func == -1:
            break
        else:
            func()

    print("\nDone")