/* 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
*/

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

// helper function needed to run leetcode problems locally
function arrayToList(arr) {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

var addTwoNumbers = function(l1, l2) {

    /* 2 4 3
       5 6 4
       ------
       7 0
         + Carry = 1

    since this is reversed its very easy

    two edge case
    a. 
       2 4
       5 null
       ------
       7 4

    b. 2 4
       3 9
       ----    
       5 3 
         + Carry 1
    */ 

    let dummy = new ListNode() // we are creating a new linked list to store the result
    let curr = dummy
    let carry = 0

    while(l1 || l2 || carry){
        const v1 = l1 ? l1.val : 0
        const v2 = l2 ? l2.val : 0

        let sum = v1 + v2 + carry
        carry = Math.floor(sum/10)
        sum = sum % 10
        curr.next = new ListNode(sum)

        // update the pointers
        curr = curr.next
        l1 = l1 ? l1.next : null
        l2 = l2 ? l2.next : null

        // if we have a carry at this point then we need one more iteration 
        // so we have carry also as one of the args in while
    }

    return dummy.next

};

console.log(addTwoNumbers(arrayToList([2,4,3]), arrayToList([5,6,2])))