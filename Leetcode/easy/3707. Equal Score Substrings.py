

class Solution:
    def scoreBalance(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        l = ord(s[0]) - ord("a") + 1
        r = sum(ord(ch) - ord("a") + 1 for ch in s) - l
        for i in range(1, len(s) - 1):
            l += ord(s[i]) - ord("a") + 1
            r -= ord(s[i]) - ord("a") + 1
            if l == r:
                return True
        return False
    

