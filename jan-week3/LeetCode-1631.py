class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        
        for i in range(len(l)):
            query=sorted(nums[l[i]:r[i]+1])
            val=True
            for j in range(2,len(query)):
                if query[0]-query[1]!=query[j-1]-query[j]:
                    val=False
                      
            answer.append(val)    
        return answer            
