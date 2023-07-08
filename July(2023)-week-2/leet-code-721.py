class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        par={i:i for i in range(n)}
        rank=[1]*n
        def find(email):
            while email!=par[email]:
                par[email]=par[par[email]]
                email=par[email]
            return email
        def union(rep1,rep2):
            par1=find(rep1)  
            par2=find(rep2) 
            if par1!=par2:
                if rank[par1]>rank[par2]:
                    par[par2]=par1
                    rank[par1]+=rank[par2]   
                else:       
                    par[par1]=par2
                    rank[par2]+=rank[par1]
        emailrep={} 
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailrep:
                    union(i,emailrep[email])
                else:
                    emailrep[email]=i    
        emailg=defaultdict(list)      
        for e,i in emailrep.items():
            owner=find(i)     
            emailg[owner].append(e) 
        res=[]    
        for i,emails in emailg.items():
            ownname=accounts[i][0]
            res.append([ownname]+sorted(emails))
        return res    




