# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # dfs tree traversal, returns height
        # of each node
        def dfs(root):

            # counting nodes not edges
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            balanced_flag = abs(right - left)

            # if current node/subtree is unbalanced or previous
            # l/r subtree unbalanced, set -1 (unbalanced flag)
            # as height of root node
            if balanced_flag > 1 or left == -1 or right == -1:
                return -1
            
            # else if subtrees and current root are balanced, set
            # height of root node
            return 1 + max(left, right)

        return dfs(root) != -1