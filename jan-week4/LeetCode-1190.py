class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=deque()
        i=0
        while(i<len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                newstack=deque()
                while(stack[-1]!='('):
                    newstack.append(stack.pop())
                stack.pop()
                stack.extend(newstack)
            i+=1
        return "".join(stack)            

         
             
