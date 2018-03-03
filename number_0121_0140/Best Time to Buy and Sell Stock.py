class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        result = 0

        if len(prices) <= 1:
            return 0

        lowest = prices[0]
        for index, price in enumerate(prices[1:]):
            if price < lowest:
                lowest = price
            else:
                profit = price - lowest
                if profit > result:
                    result = profit

        return result