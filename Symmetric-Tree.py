# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric_tree(node_a, node_b):
            if not node_a and not node_b:
                return True
            
            if node_a != None and node_b == None or node_a == None and node_b != None:
                return False
            
            if node_a.val != node_b.val:
                return False

            return symmetric_tree(node_a.left, node_b.right) and symmetric_tree(node_b.left, node_a.right)
            
        return symmetric_tree(root.left, root.right)
