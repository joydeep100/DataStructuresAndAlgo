A Binary Search Tree is a special type of tree in which

- each node can have a maximum of 2 child nodes (0-2)
- the tree is ordered, meaning the LHS of root is less then value of root, 
  and RHS of tree is greater than value at root.
  the same rule applies to all nodes

Ex. 
                 10 (root)
            
            5        15

         3    6    14    21 (leaf)


Big(O) 
insert = log(n)
searching = log(n)