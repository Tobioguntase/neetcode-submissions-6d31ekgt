class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        ans = 0

        while j <= len(prices) - 1:

            ans = max(ans,prices[j] - prices[i])
            if prices[i] > prices[j]:
                i = j
            j += 1
        return ans

        
        