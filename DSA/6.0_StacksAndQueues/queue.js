class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

class Queue{
    constructor(){
        // Its aesthetic to use first / last / size instead of head / tail / length
        this.first = null
        this.last = null
        this.size = 0
    }

    // FIFO push / shift, but we will call it enqueue / dequeue
    enqueue(val){
        let newNode = new Node(val)
        if (!this.first){
            this.first = newNode
            this.last = newNode
        } else {
            this.last.next = newNode // pointing
            this.last = newNode // mistake, forgot assigning this
        }
        return ++this.size
    }

    dequeue(){
        if (!this.first) return null

        let currHead = this.first
        
        if(this.size === 1){
            this.first = null
            // this.last = null // mistake, this is anyways null
        } else {
            this.first = currHead.next   
            // currHead.next = null // mistake, not really needed in SLL
        }
        this.size--
        return currHead
    }
}