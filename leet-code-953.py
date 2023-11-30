class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n=len(words)
        orde=[]
        for i in range(n-1):
            w1=words[i]
            w2=words[i+1]
            n1,n2=len(w1),len(w2)
            flag=False
            for j in range(min(n1,n2)):
                if w1[j]!=w2[j]:
                    print(order.index(w1[j]),order.index(w2[j]))
                    if order.index(w1[j]) >order.index(w2[j]):
                        return False
                    else:
                        flag=True
                        break
            if not flag and n1>n2:
                return False  
        return True                
