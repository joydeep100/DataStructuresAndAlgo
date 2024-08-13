/* https://leetcode.com/problems/intersection-of-two-linked-lists/
160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

*/
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var getIntersectionNode = function(headA, headB) {
    
    let ptr1 = headA
    let ptr2 = headB

    let map = new Map()

    // add all nodes into the map for any one list
    while(ptr1){
        map.set(ptr1, null) //really the value is not useful
        ptr1 = ptr1.next
    }

    // now if they intersect then obviously the the object should preexist
    while(ptr2){
        if (map.has(ptr2)){
            return ptr2
        }
        ptr2 = ptr2.next
    }
    return null
};

// little work to construct the intersecting lists, so skipping