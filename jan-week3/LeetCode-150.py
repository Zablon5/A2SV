class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque()
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                r,l=float(stack.pop()),float(stack.pop())
                if i=="/":
                    stack.append(int(l/r))
                elif i=="+":
                    stack.append(l+r)
                elif i=="-":
                    stack.append(l-r)  
                elif i=="*":
                    stack.append(l*r)   
        return int(stack.pop())                  
