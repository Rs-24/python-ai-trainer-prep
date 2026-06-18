

class Solution:
    def reverseWords(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        return " ".join(s.strip().split()[::-1])


