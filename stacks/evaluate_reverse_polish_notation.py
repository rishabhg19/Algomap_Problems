class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                if token == '+':
                    stack.append(stack.pop()+stack.pop())
                if token == '*':
                    stack.append(stack.pop()*stack.pop())
                if token == '-':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first-second)
                if token == '/':
                    divisor = stack.pop()
                    dividend = stack.pop()
                    stack.append(int(dividend/divisor))
            else:
                stack.append(int(token))
        return stack[-1]