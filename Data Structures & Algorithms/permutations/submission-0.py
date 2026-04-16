class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def backtrack(sofar, choices):
            if len(sofar) == len(nums):
                ans.append(sofar)
            
            for i in range(len(choices)):
                backtrack(sofar + [choices[i]], choices[:i] + choices[i + 1:])


        backtrack([], nums)
        return ans