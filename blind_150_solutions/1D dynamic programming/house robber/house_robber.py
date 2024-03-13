class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # greatest sum at i-2
        sum2 = 0
        # greatest sum at i-1
        sum1 = 0

        for n in nums:
            # greatest sum at i
            max_at_n = max(n + sum2, sum1)
            # move sum pointers
            sum2 = sum1
            sum1 = max_at_n

        return sum1

