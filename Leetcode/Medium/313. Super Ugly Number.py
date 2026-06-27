

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        # Time: O(n * len(primes))
        # Space: O(n + len(prices))
        u = [1] * n
        idx = [0] * len(primes)
        t = primes[:]
        for i in range(1, n):
            nxt = min(t)
            u[i] = nxt
            for j in range(len(primes)):
                if t[j] == nxt:
                    idx[j] += 1
                    t[j] = u[idx[j]] * primes[j]
        return u[-1]


