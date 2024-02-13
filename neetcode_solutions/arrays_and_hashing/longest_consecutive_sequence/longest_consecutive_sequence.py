class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        max_seq = 0

        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                current_seq = 1
                current_num = num
                while current_num+1 in numSet:
                    current_seq += 1
                    current_num += 1
                max_seq = max(max_seq, current_seq)
        return max_seq