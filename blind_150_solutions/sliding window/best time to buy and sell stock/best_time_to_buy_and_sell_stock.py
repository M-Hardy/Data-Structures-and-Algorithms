class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        max_profit = 0 

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit

    """
    Don't need to explicitly declare two pointers 
    to apply sliding window algorithm, as long as 
    you have some left and right bound. Note that 
    it's usually just the left bound being updated,
    the right bound can just iterate through the 
    collection.
    """
    def maxProfit2(self, prices):
        max_profit = 0
        lowest = prices[0]

        for price in prices:
            if price < prices:
                lowest = price
            max_profit = max(max_profit, price - lowest)
        return max_profit