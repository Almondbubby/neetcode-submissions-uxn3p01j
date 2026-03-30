class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        base cases:
        n = 0: 0
        n = 1: 1

        at each step, you can eith
        er choose to take 1 or 2
        recurrence: dp[i] = dp[i-3] + 3
        
        '''
        dp = [0 for i in range(n + 1)]
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]