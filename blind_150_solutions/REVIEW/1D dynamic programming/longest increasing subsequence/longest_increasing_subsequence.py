class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_lis_len = 1
        lis_lens = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    lis_lens[i] = max(lis_lens[i], 1 + lis_lens[j])
                    max_lis_len = max(max_lis_len, lis_lens[i])
        
        return max_lis_len