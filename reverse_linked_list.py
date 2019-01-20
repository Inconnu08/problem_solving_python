def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ls = []
    curr = head
    while curr:
        ls.append(curr.val)
        curr = curr.next

    return ls[::-1]

