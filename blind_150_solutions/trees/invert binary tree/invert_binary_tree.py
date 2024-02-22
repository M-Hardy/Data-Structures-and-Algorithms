# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return
        if root.left and not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
        if root.right and not root.left:
            root.left = self.invertTree(root.right)
            root.right = None
        if root.right and not root.left:
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
        
        return root