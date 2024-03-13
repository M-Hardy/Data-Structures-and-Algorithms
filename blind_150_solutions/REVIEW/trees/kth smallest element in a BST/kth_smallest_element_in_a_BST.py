# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        smallest = [None]
        k_val = [0]

        def dfs(root):
            
            if smallest[0] != None:
                return
            
            if not root:
                return
            
            dfs(root.left)
            k_val[0] += 1
            
            if k_val[0] == k:
                smallest[0] = root.val
                return
            
            dfs(root.right)


        dfs(root)
        return smallest[0]
    
    
    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        smallest = []

        def dfs(root):
                        
            if not root:
                return None
            
            left = dfs(root.left)
            if left:
                smallest.append(left.val)
            else:
                smallest.append(root.val)
            right = dfs(root.right)
            if right:
                smallest.append(right.val)


        dfs(root)
        print(smallest)
        return smallest[k-1]
        
