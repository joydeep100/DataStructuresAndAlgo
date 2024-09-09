/*155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
*/
var MinStack = function() {
    this.stack = []
    this.minStack = []
    this.min = Infinity

};

MinStack.prototype.push = function(val) {
    this.stack.push(val)
    
    /*  You are pushing the minimum value onto minStack only when the current value is strictly less than min. This could lead to an error 
    when popping if multiple identical minimum values are pushed, as you are not accounting for duplicates that also need to be considered 
    as minimums when popping.*/
    if (val <= this.min){
        this.min = val
        this.minStack.push(val)
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if (!this.stack.length) return null
    let val = this.stack.pop()

    if (val === this.min){
        // mistake #2 put this here [1]
        this.minStack.pop()
        
        if (!this.minStack.length){
            this.min = Infinity
        } else {
            // [1] here!!!
            this.min = this.minStack.slice(-1)[0]
        }
    }

};

/**
 * @return {number}
*/
MinStack.prototype.top = function() {
    return this.stack.slice(-1)[0]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.min
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
