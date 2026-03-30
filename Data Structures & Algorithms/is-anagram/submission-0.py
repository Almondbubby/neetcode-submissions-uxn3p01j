class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = dict()
        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in counts or counts[t[i]] == 0:
                return False
            counts[t[i]] -= 1
        for c in counts:
            if counts[c] != 0:
                return False
        return True

