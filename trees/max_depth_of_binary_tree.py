# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root == None:
            return 0
        def dfs(node, currDepth):
            if node == None:
                return currDepth
            maxDepth = max(dfs(node.left, currDepth + 1), dfs(node.right, currDepth + 1))
            return maxDepth
        return dfs(root, depth)