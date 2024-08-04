class Node {
    constructor(value) {
        this.left = null
        this.right = null
        this.value = value
    }
}

class BinarySearchTree {
    // just reusing it for execution, but remember BFS is not limited to Binary Search Tree
    constructor() {
        this.root = null
        // there is no size / length
    }

    insert(value) {
        let newNode = new Node(value)
        if (!this.root) {
            this.root = newNode
            return this
        } else {
            let current = this.root
            while (true) {
                if (value === current.value) return undefined
                if (value < current.value) {
                    if (current.left === null) {
                        current.left = newNode
                        return this
                    }
                    current = current.left

                } else {
                    if (current.right === null) {
                        current.right = newNode
                        return this
                    }
                    current = current.right

                }
            }

        }

    }

}

let tree = new BinarySearchTree()
tree.insert(10)
tree.insert(12)
tree.insert(5)
tree.insert(6)
tree.insert(100)
console.log(tree.root.right.right)