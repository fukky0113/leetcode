# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxx_depth = []

        def maximum_depth(node, depth):
            if not node:
                return

            maxx_depth.append(depth)
            maximum_depth(node.left, depth+1)
            maximum_depth(node.right, depth+1)

        if root == None:
            return 0 
        maximum_depth(root, 1)
        return sorted(maxx_depth)[-1]
