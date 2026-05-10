

class Solution:
    def fib(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n <= 1:
            return n        
        a, b = 0, 1
        for _ in range(2, n + 1):
            cur = a + b
            a = b
            b = cur
        return b


