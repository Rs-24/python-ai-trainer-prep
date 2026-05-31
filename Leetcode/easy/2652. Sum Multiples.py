

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)


