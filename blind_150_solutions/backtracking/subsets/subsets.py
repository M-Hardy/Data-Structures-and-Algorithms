class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                # have to use list() constructor pre python 3.3
                # python 3.3 and beyond - use .copy() to get 
                # copy of array
                subsets.append(list(subset))
                return

            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)

        dfs(0)
        return subsets
        