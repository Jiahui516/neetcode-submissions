class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        low=float('inf')

        for price in prices:
            low=min(price,low)
            maxProfit=max(price-low,maxProfit)
        return maxProfit