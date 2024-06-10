// IMP: if we are removing a node from LL, we need to make sure 
// its next / prev values are set to null as required (sever the connection)
class Node {
    constructor(val) {
        this.val = val
        this.prev = null
        this.next = null
    }
}

class DoublyLinkedList {

    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    push(val) {
        // add a new node at the end
        let newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            // mistake, was doing as head.next, because LL has more than 2 items head is first element right
            // so we need to do with tail
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
        return this
    }

    pop() {
        // remove the last node
        if (!this.head) return undefined
        let tail = this.tail
        if (this.length === 1) {
            this.head = null
            this.tail = null
            // this.length = 0
        } else {
            let newTail = tail.prev
            newTail.next = null
            this.tail = newTail
            tail.prev = null // this is important to remove the reference frome removed node as well
        }
        this.length--
        return tail

    }

    shift() {
        // remove a node from the beginning of LL
        if (!this.head) return undefined
        let head = this.head
        if (this.length === 1) {
            // well no need to sever (cutoff) the connection here 
            this.head = null
            this.tail = null
        } else {
            let newHead = head.next
            newHead.prev = null
            // but its important to sever the connection here
            head.next = null
            this.head = newHead
        }
        this.length--
        return head
    }

    unshift(val) {
        // add a node at the beginning of LL
        let newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            let currHead = this.head
            currHead.prev = newNode
            newNode.next = currHead
            this.head = newNode
        }
        this.length++
        return this
    }

    get(index) {
        // get a value at the given index
        if (index < 0 || index >= this.length) return null
        let current
        let count
        if (index <= Math.floor(this.length / 2)) {
            count = 0
            // first do for <= which is easy to process
            // but why <= because it is the opposite of >
            current = this.head
            while (count !== index) {
                current = current.next
                count++
            }
        }
        else {
            count = 0
            current = this.tail
            /*
            lets say LL = [0,1,2,3,4,5,6,7,8,9] and index = 7
            so, you need count = 2 right, 9->8->7
            so count should be 10 -7 (index) - 1 = 2

            there is also another nifty way of doing the same

            count = this.length - 1
            while(count !== index){
                current = current.prev
                count--
            }
            */
            while (count !== this.length - index - 1) {
                current = current.prev
                count++
            }

        }
        return current

    }

    set(index, val) {
        // recheck once, in udemy some test failed, it said circular reference error
        // update a value at the given index
        if (index < 0 || index >= this.length) return null
        let current
        let count
        if (index <= Math.floor(this.length / 2)) {
            count = 0
            current = this.head
            while (count !== index) {
                current = current.next
                count++
            }
        }
        else {
            count = this.length - 1
            current = this.tail
            while (count !== index) {
                current = current.prev
                count--
            }

        }
        current.val = val
        return current
    }

    insert(index, val) {
        // insert a node at the given index
        if (index < 0 || index >= this.length) return null

        if (index === 0) return this.unshift(val)
        if (index === this.length - 1) return this.push(val)

        let newNode = new Node(val)
        let beforeNode = this.get(index - 1)
        let afterNode = beforeNode.next //smart, same as this.get(index) right
        beforeNode.next = newNode
        newNode.prev = beforeNode
        newNode.next = afterNode
        afterNode.prev = newNode
        this.length++
        return true
    }

    remove(index) {
        // remove a nod at the given index
        if (index < 0 || index >= this.length) return undefined

        if (index === 0) return this.shift(val)
        if (index === this.length - 1) return this.pop(val)

        let removedNode = this.get(index)
        removedNode.prev.next = removedNode.next
        removedNode.next.prev = removedNode.prev
        // very IMP to sever and always a best practice to sever these
        // this was also done by Colt
        removedNode.next = null
        removedNode.prev = null
        this.length--
        return removedNode
    }
}

let list = new DoublyLinkedList()
list.push(1)
list.push(2)
list.push(3)
