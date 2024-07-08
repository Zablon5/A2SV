class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=[]
        for i in range(1,n+1):
            friends.append(i)
        ind=0
        while len(friends) > 1:
            ind = (ind + k-1) % len(friends)   
            friends.pop(ind)
        return friends[0]    
