class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsset = set(nums)
        for num in numsset:
            if num - 1 not in numsset:
                length = 1
                while num + length in numsset:
                    length += 1
                longest = max(length, longest)
        return longest