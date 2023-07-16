class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nf=0
        nt=0
        for m in bills:
            if m==5:
                nf+=1
            elif m==10:
                if nf==0:
                    return False
                nf-=1
                nt+=1
            else:
                if nf and nt:
                    nf-=1
                    nt-=1
                elif nf>=3:
                    nf-=3
                else:
                    return False
        return True 
