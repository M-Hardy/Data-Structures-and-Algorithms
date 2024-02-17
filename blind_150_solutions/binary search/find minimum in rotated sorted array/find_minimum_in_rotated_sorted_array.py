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

            if nums[m] > nums[r]:
                l = m + 1
            
            else: #== nums[m] < nums[r]
                r = m

        return nums[l]