Stack - LIFO
------------

.. A stack impemented using arrays
stack = []

.. not recommended [DO NOT IMPLEMENT STACK LIKE THIS], if we create a stack like this then it would be O(n) for adding / removing items
stack.unshift(1) // O(n)
stack.unshift(2)
.. stack = [2, 1]
stack.shift()
.. stack = []

.. we should always use push and pop
stack = []
stack.push(1)
stack.push(2)

.. stack = [1, 2]

stack.pop()

.. stack = [1]