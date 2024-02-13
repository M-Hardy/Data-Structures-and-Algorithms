class Solution(object):
    
    def getGridNumber(self, row, col):
        if 0<=row<=2:
            if 0<=col<=2:
                grid_number = 0
            if 3<=col<=5:
                grid_number = 1
            if 6<=col<=8:
                grid_number = 2
        if 3<=row<=5:
            if 0<=col<=2:
                grid_number = 3
            if 3<=col<=5:
                grid_number = 4
            if 6<=col<=8:
                grid_number = 5
        if 6<=row<=8:
            if 0<=col<=2:
                grid_number = 6
            if 3<=col<=5:
                grid_number = 7
            if 6<=col<=8:
                grid_number = 8
        
        return grid_number

    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # rows = {}
        cols = {}
        grids = {}

        for i in range(0, 9):
            cols[i] = set()
            grids[i] = set()

        for r in range(len(board)):    
            row = set()
            for c in range(len(board[r])):
                val = board[r][c]
                if val.isdigit():
                    grid_number = self.getGridNumber(r, c)                           
                    if val in row or val in cols[c] or val in grids[grid_number]:
                        return False
                    
                    row.add(val)
                    cols[c].add(val)
                    grids[grid_number].add(val)
        
        return True