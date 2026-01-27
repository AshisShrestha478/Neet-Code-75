class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minvalue = float("inf")

        for price in prices:
            if price < minvalue:
                minvalue = price
            else:
                maxprofit = max(maxprofit, price-minvalue)
        
        return 0 if maxprofit < 0 else maxprofit