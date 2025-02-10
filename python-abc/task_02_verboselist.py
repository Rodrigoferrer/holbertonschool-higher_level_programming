#!/usr/bin/python3
"""Python3"""


class VerboseList(list):
    """Class VerboseList that inherits from list"""

    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format(item))
    
    def extend(self, x):
        super().extend(x)
        print("Extended the list with {} items.".format(x))

    def remove(self, item):
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list")
        return super().pop(index)
