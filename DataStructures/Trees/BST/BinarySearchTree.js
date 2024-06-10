class Node{
    constructor(value){
        this.left = null
        this.right = null
        this.value = value
    }
}

class BinarySearchTree{
    constructor(){
        this.root = null
        // there is no size / length
    }

    insert(value){
        let newNode = new Node(value)
        if (!this.root){
            this.root = newNode
            return this // mistake, forgot to return
        }else {
            let current = this.root
            while(true){

                // we can also break a while loop by returning, instead of break

                // IMP, duplicates need to be valueidated. we will not entertain it.
                if (value === current.value) return undefined
                // handle the left side
                if (value < current.value){
                    if (current.left === null){
                        // we found our place to insert
                        current.left = newNode
                        return this
                    }
                    current = current.left
                    
                } else {
                    // else takes care of value > current.value, but we should handle === very specifically
                     if (current.right === null){
                        // we found our place to insert
                        current.right = newNode
                        return this
                    } 
                    current = current.right
                    
                }
            }
            
        }
        
    }

    find(value){
        // return true or false
        if (!this.root) return false
        let current = this.root
        let found = false
        while(current && !found){
            if (value < current.value){
                current = current.left
            }
            else if (value > current.value){
                current = current.right
            }                
            else return true
            // instead of setting found = true, we need to immidiately break the loop using return to optimize the code
        }
        return false
    }
    
}

let tree = new BinarySearchTree()
tree.insert(10)
tree.insert(12)
tree.insert(5)
tree.insert(6)
tree.insert(100)
console.log(tree.root.right.right)