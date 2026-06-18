

class Solution:
    def subsets(self, nums: list) -> list[list]:
        # Time: O(n * (2 ** n))
        # Space: O(2 ** n)
        out = [[]]
        for n in nums:
            out += [o + [n] for o in out]
        return out


