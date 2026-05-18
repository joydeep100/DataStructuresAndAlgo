class SinglyLinkedList:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
# ouside the class
def display(head):

    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next

    print(' -> '.join(res))

def search(head, val):

    curr = head
    while curr:
        if curr.val == val:
            print(f'Found {val}')
            return True
        curr = curr.next
    
    print(f'Not Found {val}')
    return False



head = SinglyLinkedList(1)
A = SinglyLinkedList(2)
B = SinglyLinkedList(3)
C = SinglyLinkedList(4)

head.next = A
A.next = B
B.next = C
print(f'Head val: {head}')

display(head)

search(head, 1)
search(head, 9)

