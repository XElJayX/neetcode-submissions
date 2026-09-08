class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { '}':'{', ']':'[',')':'('}
        for c in s:
            if c in brackets and stack and stack[-1] == brackets[c] :
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True
            
            
        