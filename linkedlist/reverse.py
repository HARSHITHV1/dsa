from linkedlist.LinkedList import LinkedList


class Reverse(LinkedList):
    def __init__(self):
        super().__init__()
        self.future = None
        self.current = None
        self.previous = None


    def reverse_list(self):
        self.previous = None
        self.current = self.head
        while self.current:
            self.future = self.current.next  # Save the next node
            self.current.next = self.previous  # Reverse the link
            self.previous = self.current  # Move previous to current
            self.current = self.future  # Move to the next node
        self.head = self.previous  # Update head to the new front of the list
        # If list is empty, tail should also be None
        if not self.head:
            self.tail = None



new_list = Reverse()  # Use Reverse class instead of LinkedList
new_list.append('str')
new_list.append('str2')
new_list.append('str3')

# Print the original list
print("Original list:")
new_list.iterate()

# Reverse the list
new_list.reverse_list()

# Print the reversed list
print("Reversed list:")
new_list.iterate()






new_list=LinkedList()
new_list.append('str')
new_list.append('str2')
new_list.append('str3')





