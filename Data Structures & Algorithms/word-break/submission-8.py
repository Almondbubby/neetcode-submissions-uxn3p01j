class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp
        dp[i] = (bool)
        '''
        dp = [False] * (len(s))

        for i in range(len(dp)):
            for w in wordDict:
                if s[i - len(w) + 1: i + 1] == w and (dp[i-len(w)] or i-len(w) + 1 == 0):
                    dp[i] = True
                    continue
        print(dp)
        return dp[-1]