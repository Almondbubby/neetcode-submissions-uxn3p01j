class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        at each step, take independently and take with last if last is not 0

        dp
        base cases:
        i = 0: dp[i] = 1 if s[0] not 0
        i = 1: dp[1] = dp[i-1] + 1 if s[1] not 0 + 1 if 1 <= s[i-1:i+1] <= 26
        
        '''

        dp = [0] * (len(s))
        dp[0] = 1 if s[0] != '0' else 0
        if len(dp) == 1:
            return dp[0]
        dp[1] = 1 if s[0] != '0' and s[1] != '0' else 0
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1
        

        for i in range(2, len(dp)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1: i + 1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
            