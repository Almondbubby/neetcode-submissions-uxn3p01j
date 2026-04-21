class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            
        sorted_counts = sorted(counts.values(), reverse=True)[:k]
        ans = []
        for num in counts:
            if counts[num] in sorted_counts:
                ans.append(num)
        return ans
