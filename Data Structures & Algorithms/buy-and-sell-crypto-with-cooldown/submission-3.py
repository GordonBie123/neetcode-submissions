class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        
        holding = -prices[0]
        sold = 0
        cooldown = 0

        for price in prices[1:]:
            previous_holding = holding
            previous_sold = sold
            previous_cooldown = cooldown

            holding = max(previous_holding, previous_cooldown - price)
            cooldown = max(previous_cooldown, previous_sold)

            sold = previous_holding  + price

        return max(sold, cooldown)
