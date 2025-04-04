'''
module of appending linked list
'''
class Node:
    '''
    Node class for reference
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    '''
    appends linked list
    '''
    current = listA
    if not current:
        return listB
    while current.next:
        current = current.next
    current.next = listB
    return listA