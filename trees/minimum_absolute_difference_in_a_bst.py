# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sortedTree = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            sortedTree.append(node.val)
            dfs(node.right)
        dfs(root)
        if not sortedTree:
            return 0
        minDiff = inf
        for i in range(1,len(sortedTree)):
            minDiff = min(minDiff, sortedTree[i]-sortedTree[i-1])
        return minDiff

            
        