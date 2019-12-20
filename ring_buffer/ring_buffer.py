from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Adding the first elements until capacity is reached
        if self.current < self.capacity: 
            self.storage.add_to_tail(item)
            self.current += 1
        # Special case that i couldn't work around, basically adding the first element after capacity is reached, or when current is reset again
        elif self.current == self.capacity:
            self.storage.delete(self.storage.head) # Delete the front of DLL
            self.storage.add_to_head(item) # Add the new item to front of DLL
            self.current += 1
        # Case to catch when current is over capacity
        else:
            current = self.storage.head # grab the head
            for i in range(self.current - self.capacity): # Loop through the amount of times that we need to shift over, EX: 6th append on 5 capacity, 6-5=1 so we shift over 1
                if current.next is not None: # is not None catches end of loop
                    current = current.next # grabs the next node
            current.insert_before(item) # Once found we insert the item before the node we found, could have done after as well, didn't really matter
            current.delete() # Deletes node that was replaced with given item
            self.current += 1
            if self.current == (self.capacity * 2): # Once current goes through the list and ends up replacing everything, we need to reset to act like its a fresh list with a fresh current
                self.current = self.capacity # Set it to capacity so it hits the second if statement above, and we are fresh

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Start at front of storage
        current = self.storage.head
        # Loop until it hits end
        while current is not None:
            list_buffer_contents.append(current.value) # Add to return array
            current = current.next # Go to next item

        return list_buffer_contents

# test = RingBuffer(7)
# test.append('a')
# test.append('b')
# test.append('c')
# test.append('d')
# test.append('e')
# test.append('f')
# test.append('g')
# test.append('h')
# test.append('i')
# test.append('j')
# print(test.get())
# test.append('k')
# test.append('l')
# test.append('m')
# test.append('n')
# test.append('o')
# print(test.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
