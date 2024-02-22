# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True

        curr_max = float('inf')
        curr_min = float('-inf')

        def validBST(root, curr_min, curr_max):
            if not root:
                return True

            if root.val <= curr_min or root.val >= curr_max:
                return False
            
            return (validBST(root.left, curr_min, root.val) and 
                    validBST(root.right, root.val, curr_max))

        return validBST(root, curr_min, curr_max) 

    
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True

        curr_max = float('inf')
        curr_min = float('-inf')

        return self.validBST(root, curr_min, curr_max) 

    def isValidBST2Helper(self, root, curr_min, curr_max):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True

        if root.val <= curr_min or root.val >= curr_max:
            return False
        
        return (self.validBST(root.left, curr_min, root.val) and 
                self.validBST(root.right, root.val, curr_max))