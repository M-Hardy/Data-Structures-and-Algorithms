# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    #iterative DFS (pre-order)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1

        while stack:
            node, level = stack.pop()
            max_depth = max(max_depth, level)

            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        
        return max_depth

    #same method, more concise
    def iterMaxDepthDFS2(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, level = stack.pop()

            if node:
                max_depth = max(max_depth, level)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        
        return max_depth


    #iterative BFS
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


    #recursive DFS (in-order)
    def maxDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)  