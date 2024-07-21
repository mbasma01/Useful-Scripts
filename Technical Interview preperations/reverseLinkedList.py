# Define ListNode class (or import from a custom module if you have one)
from ListNode import ListNode


def reverse(head):
    """
    Reverses a linked list.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        ListNode: The new head of the reversed linked list.
    """
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev  # Return the new head


# Creating the Linked List
head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)

head.next = n1
n1.next = n2

# Reversing the Linked List
new_head = reverse(head)
print(new_head.value)


