class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        queue = deque([])
        maxTime = 0

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            currx, curry, time = queue.popleft()
        
            if time > maxTime:
                maxTime = time
            
            for direction in directions:
                nx = currx + direction[0]
                ny = curry + direction[1]

                if nx < 0 or nx >= numRows or ny < 0 or ny >= numCols:
                    continue
                
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, time + 1))



        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    return -1
                    
        return maxTime
            

            

            