- To check a node exists check if (node), do not check if (node.val)

say l1 is a node.
const v1 = (l1 !== null) ? l1.val : 0 // this is valid
const v1 = (l1.val !== null) ? l1.val : 0 // this wont work