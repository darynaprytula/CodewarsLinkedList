'''
module of alterning split kata
'''
class Node(object):
    '''
    class of creating a node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''
    class that holds the two resulting lists after performing an alternating split
    '''
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    '''
    splits a given linked list into two separate linked lists
    '''
    if not head:
        raise ValueError
    if not head.next:
        raise ValueError
    last_first = None
    last_sec = None
    current = head
    new_first = None
    new_second = None
    count = 0
    while current:
        count += 1
        if count % 2 != 0:
            if new_first is None:
                new_first = current
            else:
                last_first.next = current
            last_first = current
        else:
            if new_second is None:
                new_second = current
            else:
                last_sec.next = current
            last_sec = current
        current = current.next

    if last_first:
        last_first.next = None
    if last_sec:
        last_sec.next = None
    return Context(new_first, new_second)
