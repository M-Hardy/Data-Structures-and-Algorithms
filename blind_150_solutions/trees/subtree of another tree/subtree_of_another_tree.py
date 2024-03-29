# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)


    def isSameTree(self, t1, t2):

        if not t1 and not t2:
            return True
        
        if not t1 or not t2 or t1.val != t2.val:
            return False

        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)