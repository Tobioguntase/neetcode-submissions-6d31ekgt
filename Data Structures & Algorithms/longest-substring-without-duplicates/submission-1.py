class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = 0
        dic = {s[0] : 0}
        ans = 1
       
        while j < len(s) - 1:
            
            j += 1
            if s[j] in dic.keys():
                prev = dic[s[j]]
                while i <= prev:
                    del dic[s[i]]
                    i += 1
            
            dic[s[j]] = j
            ans = max(ans, j - i + 1)

        return ans
