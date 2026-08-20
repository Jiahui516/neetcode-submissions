# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True,0)

            left_balanced,left_height=dfs(node.left)
            right_balanced,right_height=dfs(node.right)


            if not left_balanced or not right_balanced or abs(left_height-right_height)>1:
                return (False,0)

            else:
                return (True, 1+max(left_height,right_height))
        
        (isBalanced,height)=dfs(root)
        return isBalanced
