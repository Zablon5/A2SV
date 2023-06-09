class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if l<=target:
                continue
            else:
                return l
        return letters[0]            
