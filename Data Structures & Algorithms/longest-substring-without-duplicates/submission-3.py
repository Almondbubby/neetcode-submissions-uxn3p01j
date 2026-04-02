class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curlen = 0
        curstr = set()
        maxlen = 0
        left = 0
        for i in range(len(s)):
            while s[i] in curstr:
                curlen -= 1
                curstr.remove(s[left])
                left += 1
                
            curstr.add(s[i])
            curlen += 1
            if curlen > maxlen:
                maxlen = curlen
    
        if curlen > maxlen:
            maxlen = curlen

        return maxlen