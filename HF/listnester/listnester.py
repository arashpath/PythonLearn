#!/usr/bin/python
"""Python Module to print recursive list"""
def print_lol(the_list):
    """Function to Print List recursively"""
    for each_item in the_list:
        if isinstance(the_list, list):
            print_lol(each_item)
        else:
            print each_item
            