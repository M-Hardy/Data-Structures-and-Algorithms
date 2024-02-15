class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = [] #(index, height) pairs
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and (h < stack[-1][1]):
                i, prev_h = stack.pop()                
                area = prev_h * (i - i)
                max_area = max(max_area, area)
                start = i

            stack.append((start, h))

        while stack:
            (i, h) = stack.pop()
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area