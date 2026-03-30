class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s in groupings:
                groupings[s].append(word)
            else:
                groupings[s] = [word]
        ans = []
        for group in groupings:
            ans.append(groupings[group])
        return ans