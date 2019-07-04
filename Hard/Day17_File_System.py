"""
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
        dir
            subdir1
            subdir2
                file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
        dir
            subdir1
                file1.ext
                subsubdir1
            subdir2
                subsubdir2
                    file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level
sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a
file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

import os
import sys
import numpy as np


class Dir_System:
    def __init__(self, name='', parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

    def add_subdir(self, name):
        subdir = Dir_System(name=name, parent=self)
        self.subdirs.append(subdir)

    def add_file(self, name):
        self.files.append(name)


def create_file_system(str):
    name = ""
    for i, character in enumerate(str):
        if character == "\n":
            break
        name = name + character
    str = str[i+1:]

    File_sys = Dir_System(name=name, parent=None)

    name = ""
    depth = 0
    for character in str:
        if character == "\n":
            current_dir = File_sys
            for _ in range(depth - 1):
                current_dir = current_dir.subdirs[-1]
            if '.' in name:
                current_dir.add_file(name=name)
            else:
                current_dir.add_subdir(name=name)
            name = ""
            depth = 0
        elif character == "\t":
            depth += 1
        else:
            name = name + character

    if name != "":
        current_dir = File_sys
        for _ in range(depth - 1):
            current_dir = current_dir.subdirs[-1]
        if '.' in name:
            current_dir.add_file(name)
        else:
            current_dir.add_subdir(name)

    return File_sys


def paths_to_files(File_system):
    if len(File_system.subdirs) == 0 and len(File_system.files) == 0:
        return ''

    if len(File_system.subdirs) == 0:
        paths = [File_system.name + '/' + filename for filename in File_system.files]
        return paths

    if len(File_system.files) == 0:
        paths = []
        for dir in File_system.subdirs:
            paths = paths + [File_system.name + '/' + path for path in paths_to_files(dir)]

        return paths

    paths = [File_system.name + '/' + filename for filename in File_system.files]
    for dir in File_system.subdirs:
        paths = paths + [File_system.name + '/' + path for path in paths_to_files(dir)]

    return paths


def find_longest_path(str):
    File_system = create_file_system(str)
    paths = paths_to_files(File_system)
    #print(paths)
    lengths = [len(p) for p in paths]

    return max(lengths)



if __name__ == '__main__':
    str = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    assert find_longest_path(str) == 20, "Test-1 Failed"

    str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    assert find_longest_path(str) == 32, "Test-2 Failed"

    print("All tests Pass. :)")