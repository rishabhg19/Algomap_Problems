# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        def dfs(node):
            if node == None:
                return None
            dfs(node.left)
            dfs(node.right)
            temp = node.right
            node.right = node.left
            node.left = temp
        dfs(root)
        return root
        