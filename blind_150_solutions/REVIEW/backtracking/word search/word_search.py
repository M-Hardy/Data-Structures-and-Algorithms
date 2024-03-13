class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS:
                return False
            if c < 0 or c >= COLS:
                return False
            if board[r][c] != word[i]:
                return False
            if (r,c) in path:
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False