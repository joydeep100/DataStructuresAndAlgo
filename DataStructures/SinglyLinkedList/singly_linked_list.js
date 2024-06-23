/* both can be used
function Node(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}
*/

class Node{
    constructor(val){
        // mistake, was using self instead of this
        this.val = val
        this.next = null
    }
}

class SinglyLinkedList{

    constructor(){
        this.head = null,
        this.tail = null,
        this.length = 0
    }

    push(val){
        // push - add at the end of LL
        let newNode = new Node(val)
        if (!this.head){
            this.head = newNode
            this.tail = this.head
        }
        else {
            this.tail.next = newNode
            this.tail = this.tail.next // same as newNode
        }
        this.length++
        return this   // return the whole list in push
    }

    pop(){
        // pop - removes a node from the end of LL
        if (!this.head) return undefined

        let currNode = this.head
        let newTail = currNode

        if (this.length === 1){
            this.head = null
            this.tail = null
        }
        else {
         while(currNode.next){
            newTail = currNode
            currNode = currNode.next
        }
        
        newTail.next = null
        this.tail = newTail
        }
        this.length--
        return currNode
    }

    shift(){
        // shift - remove a node from the beginning of LL
        if(!this.head) return undefined
        let currNode = this.head
        this.head = currNode.next
        this.length--
        return currNode
    }

    unshift(val){
        // shift - add a node at the beginning of LL
        let newNode = new Node(val)
        if(!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            // mistake we should use else here other wise for empty LL condition
            // after the if(!this.head) it will come and execute these lines and mess up
            newNode.next = this.head 
            this.head = newNode
        }
        this.length++
        return this
    }

    get(index){
        // get a value at index
        if (!this.head || index >= this.length || index < 0) return -1
        if (index === 0) return this.head
        let count = 0
        let currNode = this.head
        while(count !== index){
            currNode = currNode.next
            count++
        }
        return currNode
    }

    set(index, val){
        // set a value at index
        if (!index || !val) return undefined
        if (!this.head || index >= this.length || index < 0) return false
        let count = 0
        let currNode = this.head
        while(count !== index){
            currNode = currNode.next
            count++
        }
        currNode.val = val
        return currNode    
    }

    insert(index, val){
        // insert a value at index
        if (!this.head) this.unshift(val)
        if(index === this.length - 1) this.push(val)

        let newNode = new Node(val)
        let currNode = this.head
        let prevNode = currNode
        let count = 0
        while(count !== index){
            prevNode = currNode
            currNode = currNode.next
            count++
        }
        newNode.next = currNode
        prevNode.next = newNode
        this.length++
        return true
    }

    remove(index){
        // insert a value at index
        if(index < 0 || index > this.length + 1 || !this.head) return false
        if (index === 0) this.shift()
        if(index === this.length - 1) this.pop()

        let prevNode = this.get(index - 1)
        let removedNode = prevNode.next
        prevNode.next = removedNode.next
        this.length--
        return removedNode
    }
    
}

let list = new SinglyLinkedList()
console.log(list.push(1))
console.log(list.get(0))
list.push(2)
list.push(3)
list.pop()
