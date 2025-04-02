'''
module of get nth node
'''
class Node:
    '''
    Node class for reference
    '''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    '''
    returns a node at a specified position in a linked list
    '''
    counter = 0
    current = node
    while current:
        if counter != index:
            counter += 1
            current = current.next
        else:
            return current
    raise ValueError
