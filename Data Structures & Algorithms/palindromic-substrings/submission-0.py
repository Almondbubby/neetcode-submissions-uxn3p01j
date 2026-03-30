class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            for j in range(i + 1):
                cur_s = s[j:i + 1]
                if cur_s == cur_s[::-1]:
                    total += 1
        return total