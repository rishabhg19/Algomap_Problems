# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = set()
        def getHeight(node):
            if not node:
                return 0
            leftHeight = 1 + getHeight(node.left)
            rightHeight = 1 + getHeight(node.right)
            return max(leftHeight, rightHeight)
        def getDiameters(node):
            if not node:
                return 0
            diameter = (getHeight(node.left)) + (getHeight(node.right))
            diam.add(diameter)
            getDiameters(node.left)
            getDiameters(node.right)
        getDiameters(root)
        return max(diam)
        