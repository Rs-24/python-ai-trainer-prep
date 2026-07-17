

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        l = h = 0
        for ch in s:
            if ch == "(":
                l += 1
                h += 1
            elif ch == ")":
                l -= 1
                h -= 1
            else:
                l -= 1
                h += 1
            if h < 0:
                return False
            l = max(l, 0)
        return l == 0


