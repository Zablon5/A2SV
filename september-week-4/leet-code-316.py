class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count=Counter(s)
        ans=[]
        seen=set()
        for i in s:
            while ans and ans[-1]>i and count[ans[-1]]>0 and i not in seen:
                
                seen.remove(ans.pop())
            if i not in seen:
                ans.append(i)
                seen.add(i)
            count[i]-=1
        return "".join(ans)
