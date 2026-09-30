class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        numRows = len(grid)
        numCols = len(grid[0])
        steps = [[0,1], [1,0], [0, -1], [-1, 0]]
        # iterate through each square and see if any of them are 1. As soon as we see a one, we run dfs on it. The dfs will turn all the squares that it passes through into 0
        def dfs(r, c):
            if r >= numRows or r < 0 or c >= numCols or c < 0 or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            for step in steps:
                dfs(r + step[0], c + step[1])
            
            
                
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    total += 1

        return total
        


