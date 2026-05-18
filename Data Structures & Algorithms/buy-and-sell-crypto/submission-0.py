class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        ls = len(prices)

        for i in range(ls):
            for j in range(1+i, ls):
                d = prices[j]-prices[i]
                res = max(res, d)
        return res

        