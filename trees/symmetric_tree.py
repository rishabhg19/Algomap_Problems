# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def invert(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                return
            invert(node.left)
            invert(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
        
        def same(node1, node2):
            if not node1 or not node2:
                if not node1 and node2:
                    return False
                if not node2 and node1:
                    return False
                return True
            left = same(node1.left, node2.left)
            right = same(node1.right, node2.right)
            return node1.val == node2.val and left and right
        
        invert(root.left)
        return same(root.left, root.right)