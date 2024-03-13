class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if not num-1 in numSet: 
                current_length = 1
                while (num+current_length) in numSet:
                    current_length += 1
                longest = max(longest, current_length)
        return longest