class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def backtrack(sofar, choices):
            ans.append(sofar)
            if len(choices) == 0: return
            for i in range(len(choices)):
                choice = choices[i]
                backtrack(sofar + [choice], choices[i + 1:])


        backtrack([], nums)
        return ans