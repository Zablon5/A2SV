class Solution:
    def simplifyPath(self, path: str) -> str:
        sp=path.split('/')
        can=[]
        for i in sp:
          
            if i=='..':
                if can:
                    can.pop()
            elif i=='':
                continue
            elif i!='.':
                can.append(i)
              
        return '/' + '/'.join(can)       
        
