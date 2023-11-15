class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
       
        l=-1
        r=-1
        i=1
        n=len(arr)
        while i<n:
            if arr[i]==arr[i-1]:
                i+=1
                continue
            if arr[i-1]>arr[i]:
                l=i-1
                r=i
            if l!=-1 and arr[i]<arr[l]:
                r=i
            i+=1    
        if l!=-1 or r!=-1:
            arr[l],arr[r]=arr[r],arr[l]
        return arr    
