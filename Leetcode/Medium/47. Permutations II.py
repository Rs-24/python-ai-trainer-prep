

class Solution:
    def permuteUnique(self, nums: list) -> list[list]:
        # Time: O(n^3)
        # Space: O(n^2)
        out = [[]]
        for n in nums:
            t = []
            for o in out:
                for i in range(len(o) + 1):
                    t.append(o[:i] + [n] + o[i:])
            out = []
            s = set()
            for p in t:
                if tuple(p) not in s:
                    s.add(tuple(p))
                    out.append(p)
        return out


