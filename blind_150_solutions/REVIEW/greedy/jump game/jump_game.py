class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] == target:
                target = i

        return target == 0
    

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """    
        target = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:

            if i + nums[i] >= target:
                target = i
            
            if target == 0:
                return True
            
            i -= 1
        
        return False