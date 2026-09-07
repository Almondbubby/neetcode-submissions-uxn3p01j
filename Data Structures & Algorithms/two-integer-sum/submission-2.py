class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sofar = dict()
        for i in range(len(nums)):
            num = nums[i]
            if target - num in sofar:
                return [sofar[target - num], i]
            sofar[num] = i
        return []