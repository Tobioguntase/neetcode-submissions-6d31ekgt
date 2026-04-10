class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)

        while low < high:
            k = (low + high) // 2

            hours = sum((p + k - 1) // k for p in piles)

            if hours <= h:
                high = k
            else: 
                low = k + 1
        
        return low
        