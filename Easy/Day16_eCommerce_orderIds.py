"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to
accomplish this, with the following API:
    * record(order_id): adds the order_id to the log
    * get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

import os
import sys
import numpy as np


class E_Commerce_log:
    def __init__(self, max_size):
        self.max_size = max_size
        self.log = []
        self.pos = 0

    def add_item(self, item):
        pass

    def get_item(self, index):
        pass

    def print_items(self):
        pass

    def __len__(self):
        return len(self.log)


def print_options():
    print("---------------------E-Comerce Log options---------------------")
    print("\t1:\tInsert an item to the log")
    print("\t2:\tGet last ith element from the log")
    print("\t3:\tPrint the entries of the log")
    print("\t4:\tPrint the options menu")
    print("\t0:\tExit")
    print("------------------------------End------------------------------")


def switch(obj, options):
    switcher = {
        0: -1,
        1: obj.add_item,
        2: obj.get_item,
        3: obj.print_items,
        4: print_options
    }
    return switcher.get(options, err_message())


def err_message():
    print("Invalid option entered")


if __name__ == '__main__':
    max_size = int(input("Please enter the maximum size of the log: "))
    eLog = E_Commerce_log(max_size)

    option = 1
    print_options()
    while option != 0:
        option = int(input("----->Please enter your option: "))
        func = switch(eLog, option)
        if func == -1:
            break
        else:
            func()

    print("\nDone")