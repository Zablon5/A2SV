class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=0
        
        freq=[]
        half=len(arr)/2
        count=Counter(arr)
        
        for j in count.values():
            freq.append(j)  
        sfreq=sorted(freq,reverse=True)
        x=len(arr)
        if len(freq)==1:
            return 1
        if len(freq)==x:
            return int(x/2)    

        for k in sfreq:
            if x-k==half:
                return c+1
            elif x-k>half:
                x=x-k
                c=c+1
            else:    
                return c+1    
