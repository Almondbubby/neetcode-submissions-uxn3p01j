class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = nums[0]
        for i in range(1, len(nums)):
            total *= nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(total//nums[i])
            else:
                ans.append(1)
                for j in range(len(nums)):
                    if j == i: continue
                    ans[-1] *= nums[j]
        return ans

