class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        poppedInd = 0
        n = len(pushed)

        for num in pushed:
            st.append(num)
            while st and st[-1] == popped[poppedInd]:
                st.pop()
                poppedInd += 1
   
        return st == []
