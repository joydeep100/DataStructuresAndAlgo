class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

let node = new Node(1)
node.next = new Node(2)
node.next.next = new Node(3)

// (1, points to 2) (2, points to 3)  (3, null)