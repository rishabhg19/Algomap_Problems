class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != 1:
                return 0
            #print(row, col, grid[row][col])
            grid[row][col] = 0
            area = 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col -1)
            return area
        
        maxArea = 0
        for r in range(m):
            for c in range(n):
                maxArea = max(maxArea, dfs(r,c))
        
        return maxArea
        