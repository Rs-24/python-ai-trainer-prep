

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return 0
        t = self.kthGrammar(n - 1, (k + 1) // 2)
        return t if k % 2 else 1 - t


