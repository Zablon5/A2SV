class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        q=deque()
        q.append((beginWord,1))
        while q:
            node,h=q.popleft()
            n=len(node)
            for i in range(n):
                for w in range(26):
                    new=node[:i]+chr(w+97)+node[i+1:]
                    if new in wordSet:
                        if new==endWord:
                            return h+1
                        q.append((new,h+1))
                        wordSet.remove(new)
        return 0
        
