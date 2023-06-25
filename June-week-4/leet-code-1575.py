class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n= len(locations)
        memo={}
        def solve(curr,remf):
            if remf<0:
                return 0
            if (curr,remf) in memo:
                return memo[(curr,remf)]
            ans=0
            if curr==finish:
                ans=1
            for nextc in range(n):
                if nextc != curr:
                    ans=(ans+solve(nextc,remf-abs(locations[curr]-locations[nextc])))%1000000007
            memo[(curr,remf)]=ans
            return ans
        return solve(start,fuel)                         
