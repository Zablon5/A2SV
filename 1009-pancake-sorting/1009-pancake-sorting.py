class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        def flip(arr,k):
          
            i=0
            j=k
            while i<=j:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1
            return arr    
           
        def nth_max(arr,n):
            curr_max=0
            curr_ind=0
            for i in range(n+1):
                if curr_max<arr[i]:
                    curr_max=arr[i]
                    curr_ind=i
                

            return (curr_max,curr_ind)
        temp=sorted(arr)   
        if temp==arr:
            return [] 
        for i in range(len(arr)-1,-1,-1):
           
            curr_mx,posn = nth_max(arr,i)
            print(curr_mx)
            flip(arr,posn)
            flip(arr,i)
            ans.append(posn+1)
            ans.append(i+1)
        return ans  