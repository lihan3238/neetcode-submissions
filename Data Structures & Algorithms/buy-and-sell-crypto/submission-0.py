class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        last=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            res=max(res,max(last,prices[i])-prices[i])
            last=max(last,prices[i])
            print(prices[i],last)
        return res
