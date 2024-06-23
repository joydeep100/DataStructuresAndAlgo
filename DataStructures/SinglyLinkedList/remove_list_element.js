function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var removeElements = function (head, val) {

    // dummy -> 1 -> -3 -> null
    // dummy is useful if we had to remove the head in case
    let dummy = new ListNode()
    dummy.next = head

    let prev = dummy, curr = head
    let nxt
    while (curr) {

        nxt = curr.next // only reason to use this is to subsitute in 2 places 

        if (curr.val === val) {
            prev.next = nxt

        } else {
            prev = curr
        }
        curr = nxt
    }

    return dummy.next
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

removeElements(arrayToList([1, 2, 3, 4]), 2)
// remove 2 from the list