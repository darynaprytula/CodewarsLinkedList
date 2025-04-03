'''
module of recursive reverse kata
'''
class Node(object):
    '''
    class of creating a node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    '''
    recursively reverse the linked list
    '''
    if not head:
        return None
    def recursive_reverse(current, previous=None):
        if not current:
            return previous
        new = current.next
        current.next = previous
        return recursive_reverse(new, current)
    return recursive_reverse(head)
