class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = (j - i) * min(heights[j], heights[i])
                if area > most:
                    most = area
        return most
                