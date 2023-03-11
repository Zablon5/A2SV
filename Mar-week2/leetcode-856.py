class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for i in s:
            if i=='(':
                stack.append(score)
                score=0
            else:
                score=stack[-1]+max(2*score,1)
                stack.pop()
        return score 
