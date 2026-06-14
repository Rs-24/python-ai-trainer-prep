

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        p = set()
        for i in range(len(s) - 1):
            p.add(s[i:i + 2])
        for i in range(len(s) - 1, 0, -1):
            if s[i - 2:i] in p:
                return True
        return False


