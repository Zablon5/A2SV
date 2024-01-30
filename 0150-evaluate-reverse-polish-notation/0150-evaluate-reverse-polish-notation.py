class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                r,l = stack.pop(),stack.pop()
                if token == '/':
                    stack.append(int(l/r))
                elif token == '+':
                    stack.append(l+r)
                elif token == '*':
                    stack.append(l*r)
                else:
                    stack.append(l-r)
                
        return int(stack.pop())