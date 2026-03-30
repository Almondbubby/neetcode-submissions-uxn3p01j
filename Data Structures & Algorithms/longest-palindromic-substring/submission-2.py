class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        dp:
        base cases:
        i = 0: s[0]

        maxlen = ..
        for j in range(i):
            s = str[j:i + 1]
            if s == s[::-1] and len(s) > maxlen:
                dp[i] = len(s)

        dp[i] = max(maxlen, )
        '''
        ans = ""
        dp = [0 for _ in range(len(s))]
        for i in range(len(dp)):
            if i == 0:
                dp[0] = 1
                ans = s[0]
            else:
                dp[i] = dp[i-1]
                for j in range(i):
                    curs = s[j:i + 1]
                    if curs == curs[::-1] and len(curs) > dp[i]:
                        dp[i] = len(curs)
                        ans = curs
        return ans