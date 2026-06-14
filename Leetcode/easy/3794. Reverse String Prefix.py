

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        return s[:k][::-1] + s[k:]


