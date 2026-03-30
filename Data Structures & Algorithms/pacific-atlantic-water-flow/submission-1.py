from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = deque()
        a = deque()

        for i in range(len(heights)):
            p.append((i,0))
            a.append((i,len(heights[i])-1))
        
        for j in range(len(heights[0])):
            p.append((0, j))
            a.append((len(heights)-1, j))
        
        p_valid = {(0, len(heights[0]) - 1), (len(heights) - 1, 0)}
        a_valid = {(0, len(heights[0]) - 1), (len(heights) - 1, 0)}

        pgrid = heights
        while p:
            pacific = p.popleft()
            for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
                i, j = pacific[0] + direction[0], pacific[1] + direction[1]
                if i >= 0 and j >= 0 and i < len(pgrid) and j < len(pgrid[i]) and pgrid[i][j] >= pgrid[pacific[0]][pacific[1]] and (i,j) not in p_valid:
                    p_valid.add((i,j))
                    p.append((i,j))


        agrid = heights
        while a:
            atlantic = a.popleft()
            for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
                i, j = atlantic[0] + direction[0], atlantic[1] + direction[1]
                if i >= 0 and j >= 0 and i < len(agrid) and j < len(agrid[i]) and agrid[i][j] >= agrid[atlantic[0]][atlantic[1]] and (i,j) not in a_valid:
                    a_valid.add((i,j))
                    a.append((i,j))


        ans = []
        for cell in p_valid:
            if cell in a_valid:
                ans.append([cell[0], cell[1]])

        return ans