class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)

        path = []



        def backtrack(targ, start):
            if targ == 0:
                ans.append(path[:])
                return
            if targ < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(targ - candidates[i], i + 1)
                path.pop()




        backtrack(target, 0)
        return ans