class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
            primes = [True] * (right + 1)
            primes[0] = primes[1] = False

            for i in range(2, int(right ** 0.5) + 1):
                if primes[i]:
                    for j in range(i ** 2, right + 1, i):
                        primes[j] = False

            primes=[i for i in range(left, right + 1) if primes[i]]
            min_d=float('inf')
            ans=[-1,-1]
            if len(primes)==1:
                return ans
            for i in range(1,len(primes)):
                if (primes[i]- primes[i-1])<min_d:
                    ans[0],ans[1]=primes[i-1],primes[i]
                    min_d=primes[i]- primes[i-1]
            return ans        
