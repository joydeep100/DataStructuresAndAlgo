class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        return f"SinglyLinkedList(length={self.length})"
    
    def display(self):
        """Display the linked list as a chain"""
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(res) if res else 'Empty List')

    def push(self, val):
        """push - add at the end of LL"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next  # same as new_node
        self.length += 1
        return self  # return the whole list in push

    def pop(self):
        """pop - removes a node from the end of LL"""
        if not self.head:
            return None

        curr_node = self.head
        new_tail = curr_node

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while curr_node.next:
                new_tail = curr_node
                curr_node = curr_node.next

            new_tail.next = None
            self.tail = new_tail

        self.length -= 1
        return curr_node

    def shift(self):
        """shift - remove a node from the beginning of LL"""
        if not self.head:
            return None
        curr_node = self.head
        self.head = curr_node.next
        self.length -= 1
        return curr_node

    def unshift(self, val):
        """unshift - add a node at the beginning of LL"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # important: use else here, otherwise for empty LL condition
            # after the if (not self.head) it will execute these lines and mess up
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        """get a value at index"""
        if not self.head or index >= self.length or index < 0:
            return -1
        if index == 0:
            return self.head
        count = 0
        curr_node = self.head
        while count != index:
            curr_node = curr_node.next
            count += 1
        return curr_node

    def set(self, index, val):
        """set a value at index"""
        if not index or not val:
            return None
        if not self.head or index >= self.length or index < 0:
            return False
        count = 0
        curr_node = self.head
        while count != index:
            curr_node = curr_node.next
            count += 1
        curr_node.val = val
        return curr_node

    def insert(self, index, val):
        """insert a value at index"""
        if not self.head:
            self.unshift(val)
        if index == self.length - 1:
            self.push(val)

        new_node = Node(val)
        curr_node = self.head
        prev_node = curr_node
        count = 0
        while count != index:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        new_node.next = curr_node
        prev_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """remove a node at index"""
        if index < 0 or index > self.length + 1 or not self.head:
            return False
        if index == 0:
            self.shift()
        if index == self.length - 1:
            self.pop()

        prev_node = self.get(index - 1)
        removed_node = prev_node.next
        prev_node.next = removed_node.next
        self.length -= 1
        return removed_node


# Test code
list_ll = SinglyLinkedList()
list_ll.push(1)
list_ll.push(2)
list_ll.push(3)
print("List after pushing 1, 2, 3:")
list_ll.display()

print(f"\nGet node at index 0: {list_ll.get(0)}")
print(f"List length: {list_ll.length}")

list_ll.pop()
print("\nList after popping:")
list_ll.display()
