from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify merging process
        dummy = ListNode(0)
        current = dummy

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Link the smaller node
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2  # Link the smaller node
                list2 = list2.next     # Move to the next node in list2
            current = current.next  # Move the current pointer to the last node

        # Append remaining nodes, if any
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the next of the dummy node
        return dummy.next

def create_linked_list(values):
    """Creates a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_list(head):
    """Prints the linked list in sorted order."""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
list1 = create_linked_list([1, 2, 4,2,1])
list2 = create_linked_list([1, 5,3, 4])

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print("Merged list in sorted order:")
print_list(merged_head)
