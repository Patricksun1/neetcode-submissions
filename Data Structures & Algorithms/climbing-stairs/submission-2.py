class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * n

        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2

            if cache[n - 1] != -1:
                return cache[n - 1]
            
            cache[n - 1] = dfs(n - 1) + dfs(n - 2)
            return cache[n - 1]
            
        return dfs(n)