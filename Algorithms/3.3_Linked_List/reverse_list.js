// https://www.youtube.com/watch?v=G0_I-ZF0S38&t=253s
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}


var reverseList = function(head) {

    /* say we have 1 -> 2 -> 3 -> null       [1]
       we need 3 -> 2 -> 1 -> null

       so we just, add a null at the beginning of [1] and reverse the links
    */

    let prev = null, curr = head
    let nxt
    while(curr){
        nxt = curr.next //storing the next [1]
        curr.next = prev // pointing it reverse
        prev = curr
        curr = nxt // using [1] here

    }

    // so when curr will point at null, then prev would point to last but one (i.e. (3)) which is our new head
    // since all links are now reversed
    return prev
    
};

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

reverseList([1,2,3,4,5])
