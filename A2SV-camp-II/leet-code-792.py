class Solution:
    def numMatchingSubseq(self, s, words):
        index = -1
        count = 0
        notSubSeq = True

        for word in words:
            for c in word:
                index = s.find(c, index + 1)
                if index == -1:
                    notSubSeq = False
                    break
            if notSubSeq:
                count += 1
            notSubSeq = True
            index = -1
        return count
