from ListNode import ListNode
def merge(head1: ListNode, head2:ListNode):
    pointer = head = ListNode()

    while(head1 and head2):
        if head1.value < head2.value:
            head.next = head1
            head1 = head1.next
        else:
            head.next = head2
            head2 = head2.next
        head = head.next

    head.next = head1 or head2

    return pointer.next

head1 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(5)

head1.next = n1
n1.next = n2

"""
while head1:
    print(head1.value, end=' ')
    head1 = head1.next

print()
"""
head2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(4)

head2.next = n3
n3.next = n4
"""
while head2:
    print(head2.value, end=' ')
    head2 = head2.next

print()
"""
new_head = merge(head1, head2)

# Printing the reversed list
current_node = new_head
while current_node is not None:
    print(current_node.value, end=' ')
    current_node = current_node.next


