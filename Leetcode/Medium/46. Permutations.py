

class Solution:
    def permute(self, nums: list) -> list[list]:
        # Time: O(n^2)
        # Space: O(n^2)
        out = []
        s = [([], nums)]
        while s:
            c, r = s.pop()
            if not r:
                out.append(c)
            for i in range(len(r)):
                s.append((c + [r[i]], r[:i] + r[i + 1:]))
        return out


