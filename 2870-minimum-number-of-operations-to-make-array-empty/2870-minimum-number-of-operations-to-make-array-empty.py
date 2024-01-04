class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        print(count)
        for i in count:
            if count[i]==1:return -1
            elif count[i]%3==0:ans+=count[i]//3
            elif count[i]==2:ans+=1
            elif count[i]%3==1:ans+=2+(count[i]-4)//3
            elif count[i]%3==2:ans+=1+(count[i]-2)//3
        return ans
        