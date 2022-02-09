from LinckedList import LinckedList

l = LinckedList(10)

def merge_sort():
    """
    Sort a linked list in ascendind order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce a sorted list until one remains 
    - Returns a linked list
    """
    #if l.size()