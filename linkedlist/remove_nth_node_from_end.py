from os.path import curdir
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        iterator = head
        while iterator:
            length += 1
            iterator = iterator.next

        if length == n:
            return head.next

        iterator = head
        for _ in range(length - n - 1):
            iterator = iterator.next
        if iterator and iterator.next:
            iterator.next = iterator.next.next

        return head


def create_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_list(head: Optional[ListNode]) -> None:

    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Initialize the Solution class
solution = Solution()

# Create a linked list from a Python list
values = [1, 2, 3, 4, 5]
n = 2
head = create_linked_list(values)
print(head)
print("Original list:")
print_list(head)

# Remove the nth node from the end
new_head = solution.removeNthFromEnd(head, n)

print(f"List after removing {n}th node from the end:")
print_list(new_head)
