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

    BFS(){ // this is done iteratively
/*         10
        6      15
      3   8       20

queue: []
visited: []

- put root in queue, call it node
- remove node from queue and put into visited []
- if node.left is present add into queue
- if node.right is present add into queue

next iteration, the first item would be processed (which is left of root) since its a queue
*/

        let queue = [] // we can implement queue using a array or linked list
        let visited = [] // this array will contain nodes in BFS order

        let node = this.root // first we take root and put it into the queue
        queue.push(node)

        while(queue.length) // till queue.length !== 0
                            // note: we put queue.length instead of queue, because in js ![] = false, so empty array [] becomes true
        {
            node = queue.shift() // remove the first element.
            visited.push(node.value) // process the first element, we can either put node or node.value for readability
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }

        return visited
    }

    DFSPreOrder(){

        let visited = []
        function traverse(node){ // helper function
            visited.push(node.value) // pushing node.value so that its easier to view the visited array in output
            if (node.left) traverse(node.left)
            if (node.right) traverse(node.right)
        }
        traverse(this.root)
        return visited
    }

    DFSPostOrder(){

        let visited = []
        function traverse(node){ // helper function
            if (node.left) traverse(node.left)
            if (node.right) traverse(node.right)
            visited.push(node.value) // pushing node.value so that its easier to view the visited array in output
        }
        traverse(this.root)
        return visited
    }

    DFSInOrder(){

        let visited = []
        function traverse(node){ // heler function
            if (node.left) traverse(node.left)
            visited.push(node.value) // pushing node.value so that its easier to view the visited array in output
            if (node.right) traverse(node.right)
        }
        traverse(this.root)
        return visited
    }

}

let tree = new BinarySearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)
/*         10
        6      15
      3   8       20  */
console.log(tree.root)
console.log(tree.BFS())            // [ 10, 6, 15, 3, 8, 20 ] done iteratively in the example

console.log(tree.DFSPreOrder())    // [ 10, 6, 3, 8, 15, 20 ] done recursively in the example
// process node, process left , process right
console.log(tree.DFSPostOrder())   // [ 3, 8, 6, 20, 15, 10 ] done recursively in the example
// process left, process right, process node
console.log(tree.DFSInOrder())     // [ 3, 6, 8, 10, 15, 20 ] done recursively in the example
// process left, process node, process right
 



