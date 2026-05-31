

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        c = 0
        for c1 in range(min(n, limit) + 1):
            for c2 in range(min(n - c1, limit) + 1):
                c += 1 if 0 <= n - c1 - c2 <= limit else 0
        return c


