class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targs = {}
        for i in range(len(nums)):
            targ = target - nums[i]
            if targ in targs:
                return [targs[targ], i]
            targs[nums[i]] = i
        return []
