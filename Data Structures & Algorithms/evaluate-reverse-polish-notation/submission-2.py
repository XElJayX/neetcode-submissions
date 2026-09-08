class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {'+','-','*','/'}

        for s in tokens:
            if s not in operand:
                stack.append(int(s))
            else:
                b = stack[-1]
                stack.pop()
                a = stack[-1]
                stack.pop()

                match s:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(a-b)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(int(a/b))
                    case _:
                        return 0
        
        return stack[-1]