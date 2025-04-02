'''
module of removing dublicates
'''
class Node(object):
    '''
    class from the task condition which initializes node for linked list
    '''
    def __init__(self, data):
        '''
        initializes instance of Node
        '''
        self.data = data
        self.next = None

def remove_duplicates(head):
    ''''
    removes dublicates from the linked list
    '''
    seen = set()
    previous = head
    if head:
        seen.add(head.data)
        current = head.next
        if not current:
            return head
        while current:
            if current.data not in seen:
                seen.add(current.data)
                previous = current
                current = current.next
            else:
                previous.next = current.next
                current = current.next
        return head
