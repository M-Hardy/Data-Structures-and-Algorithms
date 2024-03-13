class Solution(object):

    # solution for house robber 1
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum2 = 0  # greatest sum till i-2
        sum1 = 0  # greatest sum till i-1

        # at the beginning of the func,
        # sums are functionally at position
        # -1 and -2 and have sums of 0

        for i in range(len(nums)):
            # greatest sum at the current index
            tmp = max(nums[i] + sum2, sum1)
            # move sum pointers + 1
            sum2 = sum1
            sum1 = tmp

        return sum1

    # solution for house robber 2
    # kept rob as func name for test
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[0] for input array with single element
        # array with single element skipped by other 2
        # cases
        return max(nums[0], self.rob1(nums[:-1]), self.rob1(nums[1:]))
