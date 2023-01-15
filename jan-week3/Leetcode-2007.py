class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count=Counter(changed)
        answer=[]
        if len(changed)%2:
            return []
        for num in changed:
            if num==0 and count[num]>=2:
                count[num]-=2
                answer.append(num)
            elif num!=0 and count[num] and count[num*2]:
                count[num]-=1
                count[num*2]-=1
                answer.append(num)    
        if len(answer)==len(changed)//2:
            return answer
        else:
            return []        
                

  
        
        
           
