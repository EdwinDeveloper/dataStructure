import re


def binary_search(list, target):
    """
    Search in list binary model
    """
    first = 0
    last = len(list) - 1
    while first < last:
        print("Time")
        middle = (first+last)//2
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None

print("index is {} : ".format(binary_search([1,2,3,4,5,6,7,8,8,9,10,11], 17)))