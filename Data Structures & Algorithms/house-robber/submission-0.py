class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp
        base cases:
        i = 0: 0
        i = 1: nums[1]
        recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        '''
        dp = [0 for n in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = nums[0]
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        print(dp)
        return dp[-1]