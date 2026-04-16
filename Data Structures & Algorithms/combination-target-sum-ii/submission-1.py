class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)




        def backtrack(sofar, targ, start):
            if targ == 0:
                ans.append(sofar)
                return
            if targ < 0:
                return

            prev = None
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                prev = candidates[i]
                backtrack(sofar + [candidates[i]], targ - candidates[i], i + 1)




        backtrack([], target, 0)
        return ans