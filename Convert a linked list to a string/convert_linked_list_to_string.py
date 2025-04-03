'''
module of converting linked list to a string
'''
def stringify(node):
    '''
    the function converts a linked list to a string
    '''
    probe = node
    res = ''
    while probe is not None:
        res += str(probe.data)
        res += ' -> '
        probe = probe.next
    if probe is None:
        res += 'None'
    return res
