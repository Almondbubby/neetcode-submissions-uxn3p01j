class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ""


        def backtrack(left, right):
            nonlocal path
            if left > right or left < 0 or right < 0:
                return
            if left == right == 0:
                ans.append(path)
                return
            
            path += "("
            backtrack(left - 1, right)
            path = path[:-1]
            path += ")"
            backtrack(left, right - 1)
            path = path[:-1]
        backtrack(n, n)
        return ans