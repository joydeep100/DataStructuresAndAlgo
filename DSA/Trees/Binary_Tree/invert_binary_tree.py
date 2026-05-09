from basics import print_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    # Create the 3-level tree: [4, 2, 7, 1, 3, 6, 9]
    root = TreeNode(4, 
                TreeNode(2, TreeNode(1), TreeNode(3)), 
                TreeNode(7, TreeNode(6), TreeNode(9)))

    sol = Solution()
    
    print("BEFORE INVERSION:")
    print_tree(root)
    
    sol.invertTree(root)
    
    print("\nAFTER INVERSION:")
    print_tree(root)