class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr = 0 
        in_prices = prices[0]
        for i in prices[1:]:
            if i< in_prices:
                in_prices = i
            else:
                max_pr = max(max_pr, i - in_prices)
        return max_pr