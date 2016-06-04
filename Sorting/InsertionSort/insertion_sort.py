#! /usr/bin/env python3
import sys


def insertion_sort(list_):
    '''
    Sort a list of numbers by constructing a new list and
    inserting each element, as it is encountered, immediately
    preceeding the first larger element in the sorted list.
    '''
    sorted_ = []
    for item in list_:
        for index, sorted_item in enumerate(sorted_):
            if sorted_item > item:
                insert_at = index
                break
        else:
            insert_at = len(sorted_)

        sorted_.insert(insert_at, item)

    return sorted_


if __name__ == '__main__':
    args = [int(arg) for arg in sys.argv[2:]]
    print(insertion_sort(args))
