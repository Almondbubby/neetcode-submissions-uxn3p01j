class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recurse(l, r):
            if l > r:
                return -1
            median_index = ((r - l) // 2) + l
            median = nums[median_index]
            if median == target:
                return median_index
            if median < target:
                return recurse(median_index + 1, r)
            return recurse(l, median_index - 1)



        return recurse(0, len(nums) - 1)
