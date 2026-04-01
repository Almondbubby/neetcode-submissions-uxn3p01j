class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        dp
        if text1[i] == text2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1],dp[j-1])
        base cases:
            0 for i = 0 and j = 0
        '''


        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    indexi = i-1
                    indexj = j-1
                    if text1[indexi] == text2[indexj]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]