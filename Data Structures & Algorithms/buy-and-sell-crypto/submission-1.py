class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        l = 0
        r = l
        for price in prices:
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            if profit > maxprof:
                maxprof = profit
            
            r += 1
        return maxprof