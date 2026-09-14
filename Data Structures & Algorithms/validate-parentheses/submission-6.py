class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = {"]":"[", ")":"(", "}":"{"}

        for a in s:
            if a not in para:
                stack.append(a)
                
            else: 
                if stack and stack[-1] == para[a]:
                    stack.pop()
                else:
                    stack.append(a)
        
        return len(stack) == 0