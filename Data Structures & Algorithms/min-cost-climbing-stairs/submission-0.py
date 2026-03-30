class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        dp
        base cases:
        i = 0: 0
        i = 1: cost[0]
        recurrence: dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        '''
        dp = [0 for i in range(len(cost) + 1)]
        for i in range(len(cost) + 1):
            if i == 0 or i == 1: 
                dp[i] = 0
            else:
                dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        print(dp)
        return dp[-1]
