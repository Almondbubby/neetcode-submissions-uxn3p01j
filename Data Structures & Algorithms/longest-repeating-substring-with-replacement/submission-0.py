class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        curc = ''
        left = 0
        chars = set(s)

        for c in chars:
            l = 0
            count = 0
            for i in range(len(s)):
                if s[i] == c:
                    count += 1
                while (i-l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                longest = max(longest, i - l + 1)
        return longest