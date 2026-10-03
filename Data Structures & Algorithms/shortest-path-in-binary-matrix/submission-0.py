class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        if grid[0][0] == 1 or grid[numRows - 1][numCols - 1] == 1:
            return -1


        visited = set()
        queue = deque([(0, 0, 1)])
        visited.add((0, 0))


        while queue:
            r, c, currDist = queue.popleft()

            if r == numRows - 1 and c == numCols - 1:
                return currDist

            for dr, dc in directions:
                if r + dr >= numRows or r + dr < 0 or c + dc >= numCols or c + dc < 0:
                    continue
                else:
                    if (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == 0:
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc, currDist + 1))

        return -1

        
