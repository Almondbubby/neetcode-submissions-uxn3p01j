class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0
        for n in set_nums:
            if n - 1 in set_nums: continue
            cur = 1
            while n + 1 in set_nums:
                cur += 1
                n += 1
            if cur > ans: ans = cur
        return ans

