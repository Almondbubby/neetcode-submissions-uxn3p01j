class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)




        def backtrack(sofar, choices, targ):
            if targ == 0:
                ans.append(sofar)
                return
            if targ < 0:
                return

            prev = None
            for i in range(len(choices)):
                if choices[i] == prev:
                    continue
                prev = choices[i]
                backtrack(sofar + [choices[i]], choices[i + 1:], targ - choices[i])




        backtrack([], candidates, target)
        return ans