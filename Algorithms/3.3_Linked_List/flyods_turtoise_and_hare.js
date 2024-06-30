/* 141. Linked List Cycle https://leetcode.com/problems/linked-list-cycle/description/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to 
denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

1 -> 2  -> 4 
     ^     |
     |_____|
*/

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function isListCycle(head){
    /* Two ways of checking this - a. Put the object into a Map() set the count to 1, next time if we get the same key
    then we know cycle exists
    */
    let curr = head
    let map = new Map()
    let val

    // we used Map() instead of Object {} as we can have an Object itself as the key instead of a string type key
    // map[curr] = (map[curr] || 0) + 1

    while(curr){
        if (map.has(curr)){
            val = map.get(curr)
            map.set(curr, val+1)
        } else {
            map.set(curr, 1)  // O(n) and O(n)
        }   
        if (map.get(curr) > 1){
            return true
        }
        curr = curr.next
    }

    return false
}

function isListCycleFloyd(head){

    /* This is Floyd's Tortoise and Hare Algo
    so the logic is, we point 2 pointers (slow & fast to head)
    we increment slow by one node, and increment fast by 2 nodes
    if there is a cycle then slow and fast will have to meet, if there is not then fast will reach tail (null) and end the  traversal
    */
    let slow = head, fast = head

    while(fast && fast.next){

        // mistake, below 2 lines i put it after if block, in that case since both were pointing to head, return was always true
        slow = slow.next
        fast = fast.next.next

        if (slow === fast){ // O(n) and O(1)
            return true
        }
    }
    return false

}

let list = new ListNode(3)
list.next = new ListNode(2)
list.next.next = new ListNode(0)
list.next.next.next = new ListNode(-4)
list.next.next.next.next = list.next // remove this line to make it non-cycle; connect to (2)

isListCycle(list)
isListCycleFloyd(list)
