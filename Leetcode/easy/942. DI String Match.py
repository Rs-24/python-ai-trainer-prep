

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        # Time: O(n), n = len(s)
        # Space: O(n)
        l, r = 0, len(s)
        out = []
        for ch in s:
            if ch == "I":
                out.append(l)
                l += 1
            else:
                out.append(r)
                r -= 1
        out.append(l)
        return out


