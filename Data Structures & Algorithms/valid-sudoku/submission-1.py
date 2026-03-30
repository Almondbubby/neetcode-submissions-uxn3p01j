class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        threes = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in board[i][:j] + board[i][j+1:]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in threes[((i//3) * 3) + (j//3)]:
                    return False
                cols[j].add(board[i][j])
                threes[((i//3) * 3) + j//3].add(board[i][j])
        return True

                
