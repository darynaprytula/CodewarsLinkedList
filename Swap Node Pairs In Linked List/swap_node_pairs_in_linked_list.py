'''
module of the problem "Swap Node Pairs In Linked List"
'''
class Node:
    '''
    class of creating a node
    '''
    def __init__(self, next_el=None):
        self.next = next_el

def swap_pairs(head):
    '''
    swaps pairs in linked list
    '''
    current = head

    if not head:
        return head
    if not head.next:
        return head

    new_head = current.next
    previous = None
    while current and current.next:
        first_curr = current
        sec_curr = current.next
        if previous:
            previous.next = sec_curr
        first_curr.next = sec_curr.next
        sec_curr.next = first_curr
        previous = first_curr
        current = first_curr.next
    return new_head
