# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_sofar):
            if not node:
                return 0

            good_node = 0

            if node.val >= max_sofar:
                good_node += 1
            new_max = max(max_sofar, node.val)
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)
            return left + right + good_node

        return dfs(root, root.val)
