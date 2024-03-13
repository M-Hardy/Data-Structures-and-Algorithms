class Solution(object):

    # Only uses 1 binary search     
    # The trick (lesson) in this problem is to use your midpoint and l & r pointers to determine
    # which part of the array is certainly in sorted order (l -> m, m -> r), due to the pivot/rotation.
    # If you know for certain a segment is in sorted order (i.e. no pivot), then 
    # you can just check if the target is within its bounds to determine whether to 
    # keep or discard that part of the array and move your l & r pointers accordingly. 
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # everything from l -> m is in sorted order
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            # everything from m -> r is in sorted order
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                        
        return -1
    
    # Original solution - uses 2 binary searches, 1 to 
    # find pivot index, one to search correct array for 
    # target
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        min_i = self.findMinIndex(nums)
        if target > nums[-1]:
            l = 0
            r = min_i - 1
        else:
            l = min_i
            r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
        return -1


    def findMinIndex(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l += 1
            else:
                r = m
        return l

test = Solution()
print(test.search([4,5,6,7,8,1,2,3], 8))