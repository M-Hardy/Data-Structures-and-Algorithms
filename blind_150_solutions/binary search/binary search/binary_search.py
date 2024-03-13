class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            
            if nums[m] < target:
                l = m + 1
        
        return -1
