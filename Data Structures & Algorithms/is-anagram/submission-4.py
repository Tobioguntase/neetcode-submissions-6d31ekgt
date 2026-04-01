class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charCount = {}

        for i in s:
            if i in charCount:
                charCount[i] += 1
            else:
                charCount[i] = 1
        
        for i in t:
            if i in charCount:
                charCount[i] -= 1
                if charCount[i] < 0:
                    return False
            else:
                return False

        if sum(charCount.values()) == 0:
            return True  
        
        return False

       # if "".join(sorted(s)) == "".join(sorted(t)):
        #    return True
        #else:
         #   return False
        
        
