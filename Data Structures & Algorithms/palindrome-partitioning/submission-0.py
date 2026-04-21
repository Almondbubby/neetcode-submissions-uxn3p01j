class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        path = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start):
            if len("".join(path)) == len(s):
                ans.append(path[:])
                return
            
            for i in range(start, len(s)):
                if not isPalindrome(s[start:i + 1]):
                    continue
                path.append(s[start: i + 1])
                backtrack(i + 1)
                path.pop()



        backtrack(0)
        return ans



