class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par={chr(i):chr(i) for i in range(97,123)}
        rank=[1]*26
        print(par)
        print(rank)
        def find(c):
            while c!=par[c]:
                par[c]=par[par[c]]
                c=par[c]
            return c
        def union(x,y):
            parx=find(x)
            pary=find(y) 
            if parx!=pary:
                if rank[ord(parx)-97]>rank[ord(pary)-97]:
                    par[pary]=parx
                    rank[ord(parx)-97]+=rank[ord(pary)-97]
                else:
                    par[parx]=pary
                    rank[ord(pary)-97]+=rank[ord(parx)-97]
        n_eq=[]               
        for i,eq in enumerate(equations):
            firstl=eq[0]
            secondl=eq[3]
            sign=eq[1]
            
            if sign=='=':
                union(firstl,secondl)
            else:
                n_eq.append(i)    
        for i in n_eq:
            firstl=equations[i][0]
            secondl=equations[i][3]
            if find(firstl)==find(secondl):
                return False
        return True


                    

                
