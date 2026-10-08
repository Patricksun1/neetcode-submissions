class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largestProfit = 0
        start = 0

        for i in range(len(prices)):
            profit = prices[i] - prices[start]

            if profit < 0:
                start = i
            
            if profit > largestProfit:
                largestProfit = profit
            
        return largestProfit