class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestprofit = 0
        lowest = 101
        for i in range(len(prices)):
            if prices[i] - lowest > bestprofit:
                bestprofit = prices[i] - lowest
            if prices[i] < lowest:
                lowest = prices[i]
        return bestprofit
