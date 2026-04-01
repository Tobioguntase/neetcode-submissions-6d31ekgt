class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(','{','['):
                stack.append(i)
            elif i in (')','}',']'):
                if not stack: 
                    return False
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                else:
                    return False
            print(stack)
        
        if not stack:
            print(True)
            return True
        else:
            print(False)
            return False


        