# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def trav(node, maxNum):
            if not node:
                return 0

            l_sum = 0
            r_sum = 0

            if node.left:
                l_sum = trav(node.left, max(maxNum, node.val))
            if node.right:
                r_sum = trav(node.right, max(maxNum, node.val))

            if node.val >= maxNum:
                return 1 + l_sum + r_sum
            else:
                return l_sum + r_sum
            
        return trav(root, -101)