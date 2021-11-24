#!/usr/bin/env python3

import sys
import os.path

from algorithms.selection_sort import *
from algorithms.insertion_sort import *
from algorithms.bubble_sort import *
from algorithms.quicksort import *
from algorithms.merge_sort import *

def print_help():
    print(
        "USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile file that contains the numbers to be sorted, separated by space")


def check_file(file_name):
    if os.path.getsize(file_name) == 0:
        print('Empty file')
        exit(84)


def check_params(argv):
    if len(argv) != 2:
        exit(84)
    if argv[1] == '-h':
        print_help()
        exit(0)


def checkers():
    check_params(sys.argv)
    try:
        file = open(sys.argv[1], "r")
    except Exception as e:
        exit(84)
    check_file(sys.argv[1])
    return file


def get_list_from_file(file):
    content = file.read()
    content_list = content.split(" ")
    file.close()
    try:
        items = [float(item) for item in content_list]    
    except Exception as e:
        exit(84)
    return items


def display_elem(name, cmp):
    print(name + ": " + str(cmp) + " comparisons")


def display_result(items):
    if len(items) == 1:
        print(str(len(items)) + " element")
    else:
        print(str(len(items)) + " elements")
    selection = selection_sort(items[:])
    display_elem("Selection sort", selection)
    insertion = insertion_sort(items[:])
    display_elem("Insertion sort", insertion)
    bubble_nb = bubble_sort(items[:])
    display_elem("Bubble sort", bubble_nb)
    cmp_quicksort = quick_sort(items[:])
    display_elem("Quick sort", cmp_quicksort)
    cmp_merge = merge_sort(items[:])
    display_elem("Merge sort", cmp_merge)

def main():
    file = checkers()
    items = get_list_from_file(file)
    display_result(items)


if __name__ == "__main__":
    main()
