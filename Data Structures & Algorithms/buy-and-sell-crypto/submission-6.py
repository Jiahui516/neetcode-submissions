class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=prices[0]
        maxProfit=0

        for price in prices:
            if price<left:
                left=price
            profit= price-left
            maxProfit=max(maxProfit,profit)
        return maxProfit

