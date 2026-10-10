class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxp = max(maxp, prices[j] - prices[i])
        
        return maxp

# can choose not to make transaction [0]

# buy low -> sell high 
# buy first, sell has to be after

# return profit


# brute force, loop through entire array, pick the greatest difference made from one to a value after, o(n^n)?

# for loop -> second for loop iterate stuff after

