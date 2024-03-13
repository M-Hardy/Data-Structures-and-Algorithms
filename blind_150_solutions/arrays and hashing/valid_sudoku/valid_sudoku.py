class Solution(object):
   
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        cols = {}
        grids = {}

        for i in range(0, 9):
            cols[i] = set()
        
        for i in range(0, 3):
            for j in range(0, 3):
                grids[(i,j)] = set()

        for r in range(len(board)):    
            row = set()
            for c in range(len(board[r])):
                val = board[r][c]
                if val.isdigit():
                    grid_number = (r // 3, c // 3)
                    if val in row or val in cols[c] or val in grids[grid_number]:
                        return False
                    
                    row.add(val)
                    cols[c].add(val)
                    grids[grid_number].add(val)
        
        return True