class Solution:
    def isPalindrome(self, s: str) -> bool:  
        isPal = True
        stripedS = re.sub(r'[^a-zA-Z0-9\s]', '',s.replace(" ", ""))
        cleanS = stripedS.lower()
        front, end = 0, len(cleanS) - 1

        print(cleanS)

        while front < end:
            if cleanS[front] is not cleanS[end]:
                isPal = False
            front += 1
            end -= 1
        
        return isPal

        