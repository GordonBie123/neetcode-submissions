class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        total_profit = 0
        while right < len(prices):
            if prices[right] >= prices[left]:
                profit = prices[right] - prices[left]
                total_profit += profit
            left += 1
            right += 1
        return total_profit             