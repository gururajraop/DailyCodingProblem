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
import ctypes


# Each node of the linked list having a value and XOR pointer of next & prev nodes
class Node(object):
    def __init__(self, value, both=0):
        self.value = value
        self.both = both


class XOR_LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # This is to prevent garbage collection (Code adapted from Daily Coding Problem)
        self.__nodes = []

    def add_item(self):
        item = int(input("Please enter the item to be added to the list: "))
        node = Node(value=item)
        if self.head is None:
            assert (self.size == 0) and (self.tail is None), "Error!! Something wrong with the list"
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node
        self.size += 1

        # Without this line, Python thinks there is no way to reach nodes between head and tail.
        # (Code adapted from Daily Coding Problem)
        self.__nodes.append(node)

        print("Item {} added successfully to the list at position {}".format(item, self.size))

    def remove_item(self):
        print("\tIt is not possible to delete a node from the XOR linked list by only knowing the index or address.")
        print("\tFor more information check: https://en.wikipedia.org/wiki/XOR_linked_list#Drawbacks")

    def get_item(self):
        index = int(input("Please enter the position of the item: "))
        if not(0 < index <= self.size):
            print("Error!! Invalid index")
        else:
            current = self.head
            prev_id = 0
            for _ in range(index-1):
                next_id = prev_id ^ current.both
                prev_id = id(current)
                current = self._get_obj(next_id)

            print("Extracted item {} of XOR linked list from position {}".format(current.value, index))

    def print_items(self):
        print("Items in the linked list are:")
        current = self.head
        prev_id = 0
        items = [current.value]
        for _ in range(self.size-1):
            next_id = prev_id ^ current.both
            prev_id = id(current)
            current = self._get_obj(next_id)

            items.append(current.value)

        print(items)

    # (Code adapted from Daily Coding Problem)
    def _get_obj(self, id):
        return ctypes.cast(id, ctypes.py_object).value


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