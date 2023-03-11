class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for pos,spe in sorted(zip(position,speed),reverse=True):
            disleft=target-pos
            if not stack:
                stack.append(disleft/spe)
            elif stack[-1]<disleft/spe:
                stack.append(disleft/spe) 
        return len(stack)           
