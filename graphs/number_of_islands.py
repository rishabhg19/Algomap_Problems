from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = defaultdict(list)

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return 0
            grid[row][col] = '0'
            dfs(row + 1,col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            return 1

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                num_islands += dfs(r, c)
        return num_islands

        