class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        for c in s:
            if c not in word1:
                word1[c] = 1
            else:
                word1[c] += 1
        count = len(word1)
        for c in t:
            if c not in word1:
                return False
            else:
                word1[c] -= 1
                if word1[c] == 0:
                    count -= 1
                elif word1[c] < 0:
                    return False
        if count == 0:
            return True
        return False
