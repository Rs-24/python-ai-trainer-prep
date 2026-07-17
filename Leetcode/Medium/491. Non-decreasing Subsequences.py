

class Solution:
    def findSubsequences(self, nums: list) -> list[list]:
        # Time: O((2^n) * n)
        # Space: O((2^n) * n)
        s = set()
        for x in nums:
            t = set()
            for p in s:
                if x >= p[-1]:
                    t.add(p + (x,))
            t.add((x,))
            s |= t
        return [list(p) for p in s if len(p) >= 2]


