class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheapest = prices[0]
        best_profit = 0

        for price in prices[1:]:
            
            # Consider selling at today's price
            best_profit = max(best_profit, price - cheapest)

            # Update the cheapest buying price
            cheapest = min(cheapest, price)

        return best_profit


# can choose not to make transaction [0]

# buy low -> sell high 
# buy first, sell has to be after

# return profit

# O(n^2) time
# O(1) space

# brute force, loop through entire array, pick the greatest difference made from one to a value after, o(n^n)?

# for loop -> second for loop iterate stuff after

