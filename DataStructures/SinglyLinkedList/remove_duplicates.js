function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var deleteDuplicates = function (head) {

    let curr = head, nxt
    // 1 -> 1 -> 2 -> tail

    while (curr) {

        nxt = curr.next

        // mistake, logic used was (curr.next === curr.val) :) 
        // and offcourse we should also check the boundary condition right

        // second mistake, boundary check should be first, i gave (nxt.val === curr.val && nxt)
        if (nxt && nxt.val === curr.val) {
            curr.next = nxt.next
        } else {
            curr = nxt
        }
    }
    return head

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

deleteDuplicates(arrayToList([1, 1, 2]))
// should output 1,2