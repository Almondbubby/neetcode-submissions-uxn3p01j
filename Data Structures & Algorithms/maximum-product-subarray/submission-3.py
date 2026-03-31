class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        for num in nums[1:]:
            tempmax = max(num, curmax * num, curmin * num)
            curmin = min(num, curmax * num, curmin * num)
            curmax = tempmax
            if curmax > ans:
                ans = curmax
        return ans