class MaxBinaryHeap{

    constructor(){
        this.values = [41,39,33,18,27,12,55] 

        //by doing this we are skipping steps to construct the heap manually
        // we are using an array to implement heap, not we can also use a actual tree
    }

    insert(element){
        this.values.push(element)
        this.bubbleUp()
    }

    bubbleUp(){
        let idx = this.values.length - 1
        const element = this.values[idx]
        while(idx > 0){
            let parentIdx = Math.floor((idx - 1)/2)
            let parent = this.values[parentIdx]
            if (element <= parent) return
            else {
                this.values[parentIdx] = element
                this.values[idx] = parent
                idx = parentIdx
            }
        }
    }

    remove(){ // or extractMax
        // TODO
    }

    bubbleDown(){
        // TODO
    }

}

// arr = [41,39,33,18,27,12,55]
let heap = new MaxBinaryHeap()
heap.insert(55)
console.log(heap) //run in terminal

