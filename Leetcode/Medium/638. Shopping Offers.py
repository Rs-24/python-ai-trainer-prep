

from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: list, special: list[list], needs: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(price)
        @lru_cache(None)
        def dfs(state):
            t = sum(price[i] * state[i] for i in range(n))
            for s in special:
                new = list(state)
                v = True
                for i in range(n):
                    if s[i] > new[i]:
                        v = False
                        break
                    new[i] -= s[i]
                if v:
                    t = min(t, s[-1] + dfs(tuple(new)))
            return t
        return dfs(tuple(needs))


