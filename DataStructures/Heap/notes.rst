- Working mainly with Binary Heaps

Rules

- Each node can have at max 2 child nodes
- There are two types:- a. MaxBinaryHeap and b. MinBinaryHeap

MaxBinaryHeap
-------------
        41

    39       33

 18    27   12

As we can see the upper level nodes's value are aways greater than its next level.

MinBinaryHeap
-------------
        1

    3       2

 18   27      12

Just the opposite fo a MaxBinaryHeap.

*Heaps are really useful in Priority Queues*

- We can use arrays to store Binary Heaps

like so - [100, 19, 26, 17, 12, 25, 5, 6, 15, 6, 11, 13, 8, 1, 4]

                                         100
                                      19     66
                                    17  12  25  5
                                    ... and so on       
Formula
-------
a. For any index of an array n
    - the left child is stored at (2n + 1) index .Ex. 19 -> 3 & 4 which are 17 and 12
    - the right child is stored at (2n + 2) index

b. For any child node at index n
    - its parent is stored at index (Math.floor((n-1)/2))