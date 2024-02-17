class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:                     
            m = (r + l) // 2

            if nums[l-1] > nums[l]:
                return nums[l]

            if nums[m] >= nums[l]:
                l = m + 1
                        
            if nums[m] < nums[r]:
                r = m
                   
        return nums[l]