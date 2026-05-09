"""
Understanding recursion
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


"""
                       fib(5)                       --> 2^0
                      /      \
                  fib(4)    fib(3)                  --> 2^1
                 /     \    /     \                
             fib(3)  fib(2) fib(2) fib(1)           --> 2^2
             /    \   /  \   /  \
         fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)  --> 2^3
         /    \
      fib(1) fib(0)

Time complexity: O(2^n)
Space complexity: O(n) (due to the call stack, at each level of the tree we
                        have one call to fib, and the maximum depth of the tree is n)


"""

from helpers.sll import head

print(head)

def reverse(node):
    if not node:
        return

    reverse(node.next)
    print(node, end=' ')
    
reverse(head)