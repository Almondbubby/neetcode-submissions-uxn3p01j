class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area, grid = self.dfs(grid, i, j, 0)
                    if area > max_area:
                        max_area = area
        return max_area

    def dfs(self, grid, i, j, count):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != 1:
            return count, grid
        grid[i][j] = '@'
        count, grid = self.dfs(grid, i + 1, j, count)
        count, grid = self.dfs(grid, i - 1, j, count)
        count, grid = self.dfs(grid, i, j + 1, count)
        count, grid = self.dfs(grid, i, j - 1, count)
        return count + 1, grid