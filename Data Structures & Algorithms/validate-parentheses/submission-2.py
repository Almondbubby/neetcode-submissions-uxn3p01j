class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ']':'[', ')':'('}
        left = {'{','[','('}
        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                

            