#!/usr/bin/python3
"""Python3"""


class CountedIterator():
    """Class CountedIterator that heredates from iter"""

    def __init__(self, iterator, counter = 0):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
