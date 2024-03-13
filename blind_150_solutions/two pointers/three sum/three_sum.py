class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        ordered_nums = sorted(nums) #increasing order

        for i, num in enumerate(ordered_nums):
            if i and num == ordered_nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = ordered_nums[i] + ordered_nums[l] + ordered_nums[r]

                if sum == 0:
                    res.append([ordered_nums[i], ordered_nums[l], ordered_nums[r]])
                    l += 1
                    while ordered_nums[l] == ordered_nums[l-1] and l < r:
                         l += 1
                
                if sum > 0:
                    r -= 1
                
                if sum < 0:
                    l += 1

        return res