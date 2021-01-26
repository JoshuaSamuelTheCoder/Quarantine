class Solution(object):

    def wait(self, i, prices):

        min_element = prices[i]
        profit = 0
        for j in range(i+1, len(prices)):
            p = prices[j]
            min_element = min(min_element, p)
            profit = max(profit, p - min_element)

        return profit

    def maxProfitHelper(self, prices, n):

        max_profit = 0
        for i in range(n, len(prices)):
            profit = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    sell_profit = prices[j] - prices[i] + self.maxProfitHelper(prices, j+1)
                    wait_profit = self.wait(i, prices)
                    #rest_profit = self.maxProfitHelper(prices, k+1)
                    profit = max(sell_profit, wait_profit)
                    if wait_profit > sell_profit:
                        max_profit = max(max_profit, profit)
                        break
                max_profit = max(max_profit, profit)

        return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfitHelper(prices, 0)
