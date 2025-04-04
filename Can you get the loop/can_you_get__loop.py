'''
module of the problem "Can you get the loop"
'''
class Node:
    '''
    class of creating a node
    '''
    def __init__(self, next_el=None):
        self.next = next_el


def loop_size(node):
    '''
    count size of the loop in linked list
    '''
    in_loop = False
    length = 0
    fast = node
    slow = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            in_loop = True
            current = slow
            break
    if in_loop:
        start = current
        current = start.next
        while current != start:
            length += 1
            current = current.next
        return length + 1
