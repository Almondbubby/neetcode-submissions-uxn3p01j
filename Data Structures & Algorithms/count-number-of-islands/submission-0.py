class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counts = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid = self.dfs(grid, i, j)
                    counts += 1
        return counts
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != '1':
            return grid
        grid[i][j] = '@'
        grid = self.dfs(grid, i + 1, j)
        grid = self.dfs(grid, i - 1, j)
        grid = self.dfs(grid, i, j + 1)
        grid = self.dfs(grid, i, j - 1)
        return grid
