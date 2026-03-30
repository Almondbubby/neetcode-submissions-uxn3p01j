from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        freshcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append(((i,j), 0))
                elif grid[i][j] == 1:
                    freshcount += 1

        minutes = 0
        # do bfs to check
        while rotten:
            fruit = rotten.popleft()
            for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                i, j = fruit[0][0] + direction[0], fruit[0][1] + direction[1]
                if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == 1:
                    if fruit[1] + 1 > minutes:
                        minutes = fruit[1] + 1
                    rotten.append(((i,j), fruit[1] + 1))
                    grid[i][j] = 2
                    freshcount -= 1

        if freshcount > 0:
            return -1
        return minutes
        