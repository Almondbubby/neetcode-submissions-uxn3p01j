class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        base cases:
        i = 0: nums[0]
        i = 1: max(nums[1], dp[i-1])
        
        recurrence: dp[i] = max(dp[i])
        '''
        def helper(houses):
            dp = [0 for _ in range(len(houses))]
            dp[0] = houses[0]
            dp[1] = max(houses[1], dp[0])

            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]

        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(helper(nums[:-1]), helper(nums[1:]))
