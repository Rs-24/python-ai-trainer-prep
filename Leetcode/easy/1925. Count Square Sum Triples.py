

class Solution:
    def countTriples(self, n: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a ** 2 + b ** 2
                c = int(c2 ** 0.5)
                if c <= n and c * c == c2:
                    count += 1
        return count


