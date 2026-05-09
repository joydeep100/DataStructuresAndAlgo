import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

"""
A binary tree is a tree data structure in which each node has at most two children
"""

"""
TODO :: Array representation of a binary tree
"""

"""
Traversal of a binary tree can be done two ways:
1. Depth first traversal (DFS)
    a. Pre-order traversal (node, left, right)
    b. In-order traversal (left, node, right)
    c. Post-order traversal (left, right, node)
2. Breadth first traversal (BFS)


DFS
    Pre-order traversal (node, left, right)
    In-order traversal (left, node, right)
    Post-order traversal (left, right, node)

BFS
    Level order traversal (level by level)
"""

from helpers.binary_tree import A as root

print(f'Root: {root}\n')

def dfs_pre_order(node):
    if not node:
        return # can return None as well, but since we are not using the return value, we can just return without any value

    print(node, end=' ')
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)

def dfs_in_order(node):
    if not node:
        return

    dfs_in_order(node.left)
    print(node, end=' ')
    dfs_in_order(node.right)

def dfs_post_order(node):
    if not node:
        return

    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node, end=' ')

dfs_pre_order(root)
print('\n')
dfs_in_order(root)
print('\n')
dfs_post_order(root)
print('\n')

# Iterate DFS (pre-order)

def pre_order_iterative(node):
    if not node:
        return

    stack = [node]

    while stack:
        current = stack.pop()
        print(current, end=' ')

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

# BFS

from collections import deque

def bfs(node):
    if not node:
        return

    # Initialize a deque instead of a standard list
    queue = deque()
    queue.append(node)

    while queue:
        # Use popleft() for O(1) removal from the front
        current = queue.popleft()
        print(current, end=' ')

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

bfs(root)