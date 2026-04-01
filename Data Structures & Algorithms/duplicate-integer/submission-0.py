class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isdup = False

        for num in nums:
            appears = 0
            for n in nums:
                if num == n:
                    appears += 1
                if appears == 2:    
                    isdup = True
                    break  
        return isdup