

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        i = 0
        for part in p.split("*"):
            j = s.find(part, i)
            if j == -1:
                return False
            i = j + len(part)
        return True


