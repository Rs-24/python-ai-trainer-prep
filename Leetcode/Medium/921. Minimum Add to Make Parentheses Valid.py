

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        l = r = 0
        for ch in s:
            if ch == "(":
                l += 1
            else:
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l + r


