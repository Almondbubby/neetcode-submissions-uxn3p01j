from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j))
        

        while q:
            treasure = q.popleft()
            for direction in [(0,1), (1,0), (-1,0), (0,-1)]:
                i, j = treasure[0] + direction[0], treasure[1] + direction[1]
                if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == INF:
                    grid[i][j] = grid[treasure[0]][treasure[1]] + 1
                    q.append((i, j))