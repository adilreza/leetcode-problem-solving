class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime = [True for i in range(n+1)]
        p = 2
        while p*p<=n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i]=False
            p = p+1

        countt = 0
        for i in range(2,n):
            if prime[i]:
                countt = countt + 1
        return countt