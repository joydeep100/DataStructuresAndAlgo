class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

class Stack{
    constructor(){
        // Its aesthetic to use first / last / size instead of head / tail / length
        this.first = null
        this.last = null
        this.size = 0
    }

    // LIFO 
    unshit(val){
        let newNode = new Node(val)
        if (!this.first){
            this.first = newNode
            this.last = newNode
        } else {
            let tmp = this.first
            this.first = newNode
            newNode.next = tmp
            // this.last = tmp // mistake, this is tmp is anyways the tail right
        }
        return ++this.size //mistake, was doing post increment this.size++
    
        // as you can see in arr.unshift the lenght is returned after adding the val
        // so we are replicating the same
    }

    shift(){
        if (!this.first) return null

        let currHead = this.first
        if (this.size === 1){
            this.first = null
            // this.last = null // not a mistake but optimization, when only one node exist this.last would anyways be null right
        }else{

            this.first = currHead.next
            // note severing the pointers are more important in DLL
        }
        this.size--
        return currHead.val
    }
}