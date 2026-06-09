
'''
https://www.youtube.com/watch?v=EPwWrs8OtfI

                  1          <-- Level 1
                /   \
               2     3       <-- Level 2
              / \   / 
             4   5 10          <-- Level 3
'''
class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left, A.right = B, C
B.left, B.right = D, E
C.left = F

''' DFS - Prirotizes depth
                  1          <-- Level 1
                /   \
               2     3       <-- Level 2
              / \   / 
             4   5 10          <-- Level 3

             So the trvaersal will be

             1, 2, 4 (notices 4's l and r are null, goes back to 2 and then prints 5)
             5, 3, 10
DFS types    
pre-order
in-order
post-order             
'''
def pre_order(node):

    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

print('DFS - pre_order')
pre_order(A)
print('-' * 5)

def in_order(node):

    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

print('DFS - in_order')
in_order(A)
print('-' * 5)

def post_order(node):

    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

print('DFS - post_order')
post_order(A)
print('-' * 5)

# DFS can also be implemented iteratively using a stack

def pre_order_iter(node):

    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

        # the reason we append right first is since left will be on rhs
        # it would be popped first and processed

print('DFS - pre_order iterative')
pre_order_iter(A)
print('-' * 5)

# search using DFS
def search(node, target):

    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

print(search(A, 1))
print(search(A, 99))

'''
BFS - Prirotizes breadth
                  1          <-- Level 1
                /   \
               2     3       <-- Level 2
              / \   / 
             4   5 10          <-- Level 3

So traversal happens like 1, 2, 3 then 4, 5 and then 10

A BFS is impemented using queue
'''
from collections import deque

def bfs(node):

    ''' Is not aware of the levels
    Start:     queue = [1]

    Pop 1  → print 1 ,  add 2, 3       queue = [2, 3]
    Pop 2  → print 2,   add 4, 5       queue = [3, 4, 5]
    Pop 3  → print 3,   add 10         queue = [4, 5, 10]
    Pop 4  → print 4,   no children    queue = [5, 10]
    Pop 5  → print 5,   no children    queue = [10]
    Pop 10 → print 10,  no children    queue = []
    '''
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

print('BFS - normal')
bfs(A)
print('-' * 5)

def bfs_level_order(node):
    '''
    Start:  queue = [1]
    --- Iteration 1 ---
    level_size = len(queue) = 1
    Pop 1  → add 2, 3        queue = [2, 3]
    Level 1 done → [1]

    --- Iteration 2 ---
    level_size = len(queue) = 2
    Pop 2  → add 4, 5        queue = [3, 4, 5]
    Pop 3  → add 10          queue = [4, 5, 10]
    Level 2 done → [2, 3]

    --- Iteration 3 ---
    level_size = len(queue) = 3
    Pop 4  → no children     queue = [5, 10]
    Pop 5  → no children     queue = [10]
    Pop 10 → no children     queue = []
    Level 3 done → [4, 5, 10]
    '''

    if not node:
        return
    
    q = deque([node]) # or can append separately
    level = 1
    
    while q:

        for _ in range(len(q)):

            node = q.popleft()
            print(f'L{level}->{node.val}')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        level += 1


print('BFS - level aware')
print(bfs_level_order(A))