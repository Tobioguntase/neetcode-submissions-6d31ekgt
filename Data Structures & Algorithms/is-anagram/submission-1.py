class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        isAn = True
        
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        else:
            return False
        
        
