class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

head.next = A
A.next = B
B.next = C