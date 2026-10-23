class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,profit=float('inf'),0
        for x in prices:
            low=min(low,x)
            profit=max(profit,x-low)
        return profit
