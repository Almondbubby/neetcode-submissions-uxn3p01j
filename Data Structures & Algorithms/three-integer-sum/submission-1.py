class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    two = nums[j] + nums[k]
                    if nums[i] + two == 0:
                        ans.append(sorted([nums[i], nums[j], nums[k]]))
        unique_data = []
        for item in ans:
            if item not in unique_data:
                unique_data.append(item)
        return unique_data



