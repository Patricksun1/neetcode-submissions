class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque([(0, 0, 1)])
        directions = [[0,1], [1, 0], [-1,0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        visited.add((0, 0))
        n = len(grid)   

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        while queue:
            currx, curry, dist = queue.popleft()

            if currx == n - 1 and curry == n - 1:
                return dist
    

            for direction in directions:
                nx = currx + direction[0]
                ny = curry + direction[1]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        
        return -1






        
