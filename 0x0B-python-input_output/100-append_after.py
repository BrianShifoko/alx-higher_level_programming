#!/usr/bin/python3
""" Program that search and update a file """


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file, after
    each line containing a specific string """
    str = ""
    with open(filename, 'r') as f:
        for line in f:
            str += line
            if (search_string in line):
                str += new_string
    with open(filename, 'w') as f:
        f.write(str)
