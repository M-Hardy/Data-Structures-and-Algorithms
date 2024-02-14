class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = [] #[index, height]
        max_area = 0

        for i, height in enumerate(heights):
            current_height = [i, height]

            while stack and (height < stack[-1][1]):
                prev_index, prev_height = stack.pop()
                prev_height_area = prev_height * (i - prev_index)
                # print(prev_height, prev_height_area)
                max_area = max(max_area, prev_height_area)
                if prev_height >= current_height[1]:
                    current_height[0] = prev_index

            stack.append(current_height)

        while stack:
            [index, height] = stack.pop()
            area = height * (len(heights) - index)
            # print(height, area)
            max_area = max(max_area, area)

        return max_area