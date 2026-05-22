

class Solution:
    def cellsInRange(self, s: str) -> list:
        # Time: O(n^2)
        # Space: O(n^2)
        out = []
        for c in range(ord(s[0]), ord(s[3]) + 1):
            for r in range(int(s[1]), int(s[4]) + 1):
                out.append(chr(c) + str(r))
        return out


