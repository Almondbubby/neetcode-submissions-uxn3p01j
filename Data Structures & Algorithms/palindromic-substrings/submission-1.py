class Solution:
    def countSubstrings(self, s: str) -> int:


        t = '#' + '#'.join(s) + '#'
        p = [0] * len(t)
        l = r = 0
        total = 0
        for i in range(len(t)):
            if i < r:
                p[i] = min(r-i, p[l + (r-i)])
                total += 1
            else:
                p[i] = 0
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < len(t) and t[i+p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
                total += 1
            if i + p[i] > r:
                r = i + p[i]
                l = i - p[i]
        ans = 0
        for length in p:
            ans += (length + 1) // 2
        return ans
