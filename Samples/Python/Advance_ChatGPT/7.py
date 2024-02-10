# Program: Implement a binary tree and a method to find the height of the tree.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        return max(left_height, right_height) + 1

# Test case
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(height(root))  # Expected output: 3
