class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n
        
        one_step = 1
        two_steps = 2
        res = 0

        for i in range(3, n + 1):
            res = one_step + two_steps
            one_step = two_steps
            two_steps = res
        return res

    
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        steps = [0] * n
        steps[0] = 1
        steps[1] = 2

        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n-1]
