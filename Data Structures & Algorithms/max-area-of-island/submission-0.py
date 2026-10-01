class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxVal = 0
        numRows = len(grid)
        numCols = len(grid[0])
        steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if r >= numRows or r < 0 or c >= numCols or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr, dc in steps:
                area += dfs(r + dr, c + dc)

            return area

        
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    size = dfs(i, j)
                    if size > maxVal:
                        maxVal = size

        return maxVal




