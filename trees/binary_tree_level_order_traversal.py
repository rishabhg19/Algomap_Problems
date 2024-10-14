# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        level = []
        while q:
            while q:
                level.append(q.popleft())
            for node in level:
                if node:
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
            result.append([node.val for node in level if node])
            level.clear()
        return result[:-1]



        