class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        i = len(nums) - 1
        while goal > 0 and i >= 0:
            if goal - i <= nums[i]:
                goal = i
            i -= 1
        if goal <= 0:
            return True
        return False