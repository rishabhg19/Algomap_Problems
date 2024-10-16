# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, pathSum):
            if not node:
                return False
            if pathSum + node.val == targetSum and node.left == None and node.right == None:
                return True
            print(pathSum + node.val)
            currSum = pathSum + node.val
            rightHasSum = dfs(node.right, currSum)
            leftHasSum = dfs(node.left, currSum)
            return rightHasSum or leftHasSum
        return dfs(root, 0)