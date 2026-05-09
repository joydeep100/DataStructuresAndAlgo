'''Design a stack that supports push, pop, top, and retrieving the minimum element 
*** in constant time ***

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

# Naive approach

class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk) # this is O(n)
    
# to do in O(1) we have to keep another stack called (self.min_stack)
# and keep appending unique min values, at any point its top would be the min val

# *** here the most important thing is we append a value when
# val <= self.min_stack[-1], so not only the smaller one even if its same value
# we still append it, else if we push -2, -3 and -3 and we pop -3 we would incorrectly
# get -2 as min instead of -3

class MinStackOpt:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]