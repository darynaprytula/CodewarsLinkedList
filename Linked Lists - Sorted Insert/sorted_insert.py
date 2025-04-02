'''
module of sorted inserting kata
'''
class Node(object):
    '''
    class of creating a node
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    '''
    inserts a new node into a sorted linked list
    '''
    inserted = Node(data)
    current = head
    if not current:
        head = inserted
        return head
    if data < current.data:
        inserted.next = current
        return inserted
    while current.next and current.next.data < data:
        current = current.next
    inserted.next = current.next
    current.next = inserted
    return head
