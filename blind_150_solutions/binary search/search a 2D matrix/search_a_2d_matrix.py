class Solution(object):   
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            row = matrix[mid]
            
            if row[0] == target or row[-1] == target:
                return True

            elif row[0] > target:
                end = mid - 1
            
            elif row[-1] < target:
                start = mid + 1

            elif row[0] < target and row[-1] > target:
                return self.binarySearch(row, target)

        return False
    
    def binarySearch(self, row, target):
        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if row[m] == target:
                return True

            if row[m] < target:
                l += 1
            
            if row[m] > target:
                r -= 1
        
        return False