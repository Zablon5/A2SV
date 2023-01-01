#User function Template for python3

class Solution: 
    
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            imin=i
            for j in range(i+1,n):
                if arr[j]<arr[imin]:
                    imin=j
            arr[i],arr[imin]=arr[imin],arr[i]       
