class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans=[]
        def sieve_of_eratosthenes(limit):
            primes = [True] * (limit + 1)
            primes[0] = primes[1] = False

            for i in range(2, int(limit ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, limit + 1, i):
                        primes[j] = False

            prime_numbers = []
            for i in range(2, limit + 1):
                if primes[i]:
                    prime_numbers.append(i)

            return prime_numbers
        p=sieve_of_eratosthenes(n)
        l=0
        r=len(p)-1
        while l<=r:
            if p[l]+p[r]==n:
                ans.append([p[l],p[r]])
                l+=1
                r-=1
            elif p[l]+p[r]>n:
                r-=1
            elif p[l]+p[r]<n:
                l+=1
        return ans    
