class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            else:
                profit = prices[i]-mini
                max_profit = max(max_profit,profit)
        return max_profit
        