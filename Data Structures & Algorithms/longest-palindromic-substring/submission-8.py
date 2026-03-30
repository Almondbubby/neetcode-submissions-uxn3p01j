class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        manacher
        1. preprocess
        2. loop through
            3. if index is within bounds of current palindrome, set p[i] to min of mirrored and rest of bound
            4. otherwise p[i] = 0
            5. increment p[i] based on if palindromic beyond bounds of current palindrom
            6. update bounds as necessary
        7. return the max of p
        '''


        t = '#' + '#'.join(s) + '#'
        p = [0] * len(t)
        l = r = 0
        for i in range(len(t)):
            if i < r:
                p[i] = min(r-i, p[l + (r-i)])
            else:
                p[i] = 0
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < len(t) and t[i+p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            if i + p[i] > r:
                r = i + p[i]
                l = i - p[i]

        center = 0
        length = 0
        for i in range(len(p)):
            if p[i] > length:
                length = p[i]
                center = i
        return s[(center - length) // 2 : ((center - length) // 2) + length]

