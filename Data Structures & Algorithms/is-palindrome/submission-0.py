class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        news = ""
        for i in range(len(s)):
            if s[i].isalnum():
                news += s[i]
        return news == news[::-1]