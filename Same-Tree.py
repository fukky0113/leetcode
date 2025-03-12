# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []
        def inorder(node, arr):
            if not node:
                arr.append(None)
                return
            
            arr.append(node.val)
            inorder(node.left, arr)
            inorder(node.right, arr)

        inorder(p, p_arr)
        inorder(q, q_arr)
        return p_arr == q_arr
