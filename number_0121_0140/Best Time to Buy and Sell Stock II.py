class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        result = 0
        for index, price in enumerate(prices[1:],1):
            if price > prices[index-1]:
                result += price - prices[index-1]

        return result