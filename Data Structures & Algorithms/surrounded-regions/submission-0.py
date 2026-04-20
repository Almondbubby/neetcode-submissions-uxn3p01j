from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1):
                    q.append((i, j))
        
        safe = set()
        while q:
            cur = q.popleft()
            safe.add(cur)
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for direction in directions:
                new = (direction[0] + cur[0], direction[1] + cur[1])
                if new not in safe  and new[0] >= 0 and new[0] < len(board) and new[1] >= 0 and new[1] < len(board[0])and board[new[0]][new[1]] == 'O':
                    q.append(new)

                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in safe and board[i][j] == 'O':
                    board[i][j] = 'X'
