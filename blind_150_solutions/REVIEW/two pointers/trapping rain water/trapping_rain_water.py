"""
This problem is initially unintuitive, but it is
basically an extension of the container with most 
water problem. 

As with the previous problem: A container is
defined by a left and a right boundary, and its
volume is defined by the minimum height of its
boundaries. 

The trick with this problem is that you define 
each height as a container. 

.... (until you can explain what the heart of the 
problem is in a single sentence, you don't have 
an intuitive understanding of it yet. same goes
with explaining a corresponding solution.)
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0 
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        water = 0

        while l < r:
                        
            if l_max == min(l_max, r_max):
                l += 1          
                l_max = max(l_max, height[l])  
                water += l_max - height[l]

            elif r_max == min(l_max, r_max):
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]
        
        return water