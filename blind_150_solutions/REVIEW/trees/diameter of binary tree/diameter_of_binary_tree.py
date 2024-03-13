# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_diameter = [0]

        def dfs(root):
            
            # height of empty node is -1; height 
            # of node with no children is 0. height
            # is a measure of how many edges node
            # has (not how many nodes)
            if not root:
                return -1
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            max_diameter[0] = max(max_diameter[0], 2 + left_height + right_height)
            root_height = 1 + max(left_height, right_height)
            return root_height

        dfs(root)
        return max_diameter[0]
    
    
    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # global variable needs to be 
        # non-primitive or else a local 
        # copy will be used by nested func
        max_diameter = [0]

        def dfs(root):
            
            if not root:
                return 0
            
            left_path_height = dfs(root.left)
            right_path_height = dfs(root.right)
            max_diameter[0] = max(max_diameter[0], left_path_height + right_path_height)
            root_height = 1 + max(left_path_height, right_path_height)
            return root_height

        dfs(root)
        return max_diameter[0]