class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr=[0]*(n+1)
        
        if n==0:return 0
        if n==1:return 1
        arr[1]=1
        for i in range(2,n+1):
            
            if i%2==0:
                arr[i]=arr[i//2]
            else:
                arr[i]=arr[(i-1)//2]+arr[(i-1)//2 +1 ]
        return max(arr)       
