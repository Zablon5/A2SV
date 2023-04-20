class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans=float('inf')
        bucket=[0]*k
        def backtrack(pos):
            nonlocal ans,bucket
            if pos==len(cookies):
                ans=min(ans,max(bucket))
                return
            if ans<=max(bucket):
                return
            for i in range(k) :
                bucket[i]+=cookies[pos]
                backtrack(pos+1)
                bucket[i]-=cookies[pos]
                if bucket[i]==0:
                    break
        backtrack(0)
        return ans           
