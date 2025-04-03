'''
module of parsing linked list from a string
'''
class Node:
    '''
    class from the task condition which initializes node for linked list
    '''
    def __init__(self, data, next=None):
        '''
        initializes instance of Node
        '''
        self.data = data
        self.next = next

def linked_list_from_string(s):
    '''
    gets linked list from a string
    '''
    string = s.split(' -> ')[:-1]
    head = None
    for el in string[::-1]:
        head = Node(int(el), head)
    return head
