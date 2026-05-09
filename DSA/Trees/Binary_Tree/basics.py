
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(node, indent=0):
    if node:
        print_tree(node.right, indent + 8)
        print(" " * indent + "──>", node.val)
        print_tree(node.left, indent + 8)

if __name__ == "__main__":

    """
                  4          <-- Level 1
                /   \
               2     7       <-- Level 2
              / \   / \
             1   3 6   9     <-- Level 3
    """
    # Level 1
    root = TreeNode(4)
    # Level 2
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    # Level 3
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Print as array
    print_tree(root)