'''
module of push & build one two three
'''
class Node:
    '''
    class from the task condition which initializes node for linked list
    '''
    def __init__(self, data):
        '''
        initializes instance of Node
        '''
        self.data = data
        self.next = None

def push(head, data):
    '''
    adds a new node with the given data to the top of the list
    '''
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    '''
    creates a linked list of three nodes with values 1 -> 2 -> 3
    '''
    initial = Node(3)
    second = push(initial, 2)
    final =  push(second, 1)
    return final
