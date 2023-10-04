class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hmap={}
        for w in words2:
            minihmap={}
            for i in w:
                if i in minihmap:
                    minihmap[i]+=1
                else:
                    minihmap[i]=1    
            for j in minihmap:
                if j in hmap:
                    hmap[j]=max(minihmap[j],hmap[j])    
                else:
                    hmap[j]=minihmap[j]  
        x=words1.copy()                
        for k in x:
            count=Counter(k)
            print(count)
            print(hmap)
            for i in hmap:
                if i not in count:
                    words1.remove(k)
                    break
                elif count[i]<hmap[i]:
                    words1.remove(k)
                    break
        return words1 
