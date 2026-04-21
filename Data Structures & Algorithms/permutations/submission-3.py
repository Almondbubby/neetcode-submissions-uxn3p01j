class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        path = []


        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return


            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i-1]):
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                used[i] = False
                path.pop()


        backtrack()
        return ans
            

