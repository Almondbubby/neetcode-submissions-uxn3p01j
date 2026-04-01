class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp
        take up + left + 2
        '''


        dp = [[0] * n] * m
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]