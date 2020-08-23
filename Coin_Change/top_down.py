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
