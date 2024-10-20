# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        treeList = []
        def validate(node):
            if not node:
                return
            leftSubtree = validate(node.left)
            treeList.append(node.val)
            rightSubtree = validate(node.right)
        validate(root)
        for i in range(1, len(treeList)):
            if treeList[i] <= treeList[i-1]:
                return False
        return True
            
            
        