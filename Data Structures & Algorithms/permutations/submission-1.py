class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        used = [False] * len(nums)

        def backtrack(sofar):
            if len(sofar) == len(nums):
                ans.append(sofar)
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                backtrack(sofar + [nums[i]])
                used[i] = False


        backtrack([])
        return ans