class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=-prices[0]
        rest=0
        sold=float("-inf")

        for price in prices[1:]:
            oldhold=hold
            oldrest=rest
            oldsold=sold

            hold=max(oldhold,oldrest-price)
            rest=max(oldrest,oldsold)
            sold=oldhold+price
        
        return max(sold,rest)
