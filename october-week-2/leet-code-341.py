# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.i=-1

        def rec(nestedInteger):
            flattened=[]
            for value in nestedInteger:
                if value.isInteger():
                    flattened.append(value.getInteger())
                else:
                    flattened.extend(rec(value.getList()))
            return flattened        
        self.fl=rec(nestedList)       
        self.n=len(self.fl)
    def next(self) -> int:
        self.i+=1
        return self.fl[self.i]

    def hasNext(self) -> bool:
        if self.i<self.n-1:
            return True
        return False
