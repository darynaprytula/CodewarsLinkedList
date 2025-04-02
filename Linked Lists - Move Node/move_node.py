'''
module of moving node kata
'''
class Node(object):
    '''
    class of creating a node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''
    class to store the state of the source and destination linked lists.
    '''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''
    moves the first node from the source linked list to the front of the destination linked list
    '''
    if not source:
        raise ValueError
    moved = source
    source = source.next
    new_dest = moved
    new_dest.next = dest
    return Context(source, new_dest)
