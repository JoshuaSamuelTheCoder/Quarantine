"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def dp(self, num, amount):


        if num < 0:
            return float("inf")
        elif num == 0:
            return amount
        else:
            if num not in self.seen:
                minAmount = float("inf")
                for c in self.coins:
                    minAmount = min(minAmount, self.dp(num-c, amount) + 1)

                self.seen[num] = minAmount
                return minAmount
            else:
                return self.seen[num]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.seen = {}
        self.answer = amount
        self.coins = coins
        ans = self.dp(amount,0)
        return -1 if ans == float("inf") else ans
