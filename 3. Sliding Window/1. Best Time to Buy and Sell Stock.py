class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
            
        purchase_price = prices[0]
        highest_profit = 0

        for price in prices:
            if price < purchase_price:
                purchase_price = price
                continue

            profit = price - purchase_price

            if profit > highest_profit:
                highest_profit = profit

        return highest_profit

sol = Solution()
print(sol.maxProfit(prices = [7, 1, 5, 3, 6, 4])) # Output: 5
print(sol.maxProfit(prices = [7, 6, 4, 3, 1])) # Output: 0
