class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        s1, s2 = 0, 0 
    
        for c in cost:
            curr = c + min(s1, s2)
            s1, s2 = s2, curr
        
        return min(s1, s2)
        