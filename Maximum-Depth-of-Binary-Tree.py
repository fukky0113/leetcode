# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maximum_depth(node, depth):
            if not node:
                return depth
            return max(maximum_depth(node.left, depth+1), maximum_depth(node.right, depth+1))
        return maximum_depth(root, 0)
