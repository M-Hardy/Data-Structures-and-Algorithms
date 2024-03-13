class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = float('-inf')
        curr_sum = float('-inf')

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum