# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        RES = 0
        def helper(node, s):
            nonlocal RES
            if(node.left == None and node.right == None):
                RES += s*10 + node.val
            elif(node.left == None):
                helper(node.right, s*10+node.val)
            elif(node.right == None):
                helper(node.left, s*10+node.val)
            else:
                helper(node.right, s*10+node.val)
                helper(node.left, s*10+node.val)

        if(not root):
            return 0
        helper(root, 0)
        return RES
