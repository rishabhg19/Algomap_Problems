# Leetcode 121 Best time to buy and sell stock
# Algomap Arrays and Strings 5
# Trick - track minimim price so far and max_profit so far
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10000
        max_profit = -10000
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if i >= 1 and (prices[i] - minPrice) > max_profit:
                max_profit = prices[i] - minPrice
        return max(max_profit,0)