# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        def same(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if node1.val != node2.val:
                return False
            leftSubtreeSame = same(node1.left, node2.left)
            rightSubtreeSame = same(node1.right, node2.right)
            sameValue = node1.val == node2.val
            return sameValue and leftSubtreeSame and rightSubtreeSame
        def dfs(node):
            if same(node, subRoot):
                return True
            if not node:
                return False
            subtreeSame = same(node.right, subRoot) or same(node.left, subRoot)
            return subtreeSame or dfs(node.right) or dfs(node.left)
        return dfs(root)

        # node1 = TreeNode()
        # node1.val = 4
        # node1.left = TreeNode()
        # node1.right = TreeNode()
        # node1.left.val = 1
        # node1.right.val = 2
        # print(same(subRoot, node1))

                # node1 = TreeNode()
        # node1.val = 1
        # node1.right = TreeNode()
        # node1.right.val = 1
        # node1.right.left = TreeNode()
        # node1.right.left.val = 2
        # node2 = TreeNode()
        # node2.val = 1
        # node2.right = TreeNode()
        # node2.right.val = 1
        # node2.right.left = TreeNode()
        # node2.right.left.val = 2
        #print(dfs(node1,node2))