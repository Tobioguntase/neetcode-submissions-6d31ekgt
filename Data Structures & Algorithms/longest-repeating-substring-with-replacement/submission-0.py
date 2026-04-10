class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxL = 0
        maxF = 0        
        front = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxF = max(maxF, count[s[end]])

            while (end  - front + 1) - maxF > k:
                count[s[front]] -= 1
                front += 1
            
            maxL = max(maxL, end - front + 1)
        
        return maxL