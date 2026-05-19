

class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n //= 2
            else:
                count += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return count


