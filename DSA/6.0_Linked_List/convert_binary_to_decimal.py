# Helper code to run leetcode solutions locally
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Actual code
def get_decimal_value(list):

    head = list
    res = 0
    while(head):
        # basically this formula works
        res = 2 * res + head.val
        head = head.next

    return res

print(get_decimal_value(array_to_list([1,0,1,0]))) #10
print(get_decimal_value(array_to_list([1,0,1,1]))) #11