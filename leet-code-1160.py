class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        m=len(chars)
        ans=0
        chars=''.join(sorted(chars))
        for word in words:
            n=len(word)
            word=''.join(sorted(word))
            i=0
            j=0
            while i<n and j<m:
                if word[i]==chars[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
           
            if i==n:
                ans+=n
        return ans
