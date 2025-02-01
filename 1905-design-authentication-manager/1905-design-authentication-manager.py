class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.hmap = {} #token:expiry time
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hmap[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hmap and self.hmap[tokenId] > currentTime:
            self.hmap[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
       
        for token in self.hmap:
            if self.hmap[token] > currentTime:
                ans += 1
        return ans


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)