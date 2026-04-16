class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []



        def backtrack(sofar, targ, choices, start):
            if targ == 0:
                ans.append(sofar)
            if targ < 0:
                return
            for i in range(start, len(choices)):
                choice = choices[i]
                backtrack(sofar + [choice], targ - choice, choices, i)



        backtrack([], target, nums, 0)
        return ans