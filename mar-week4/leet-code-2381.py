class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
                prefix = [0] * (len(s) + 1)
                for start, end, direction in shifts:
                    if direction == 1:
                        prefix[start] += 1
                        prefix[end + 1] -= 1
                    else:
                        prefix[start] -= 1
                        prefix[end + 1] += 1
                for i in range(1,len(s)+1):
                    prefix[i]+=prefix[i-1]
                res=[]
                for i,c in enumerate(s):
                    change=(ord(c)-97+prefix[i])%26

                    res.append(chr(change+97))
                return ''.join(res)    
