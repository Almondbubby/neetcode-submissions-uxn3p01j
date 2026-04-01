class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
    
        for j in range(len(nums)):           
            for i in range(target, 0, -1):   
                if i - nums[j] >= 0 and dp[i - nums[j]]:
                    dp[i] = True
    
        return dp[-1]