

class Solution:
    def sortByReflection(self, nums: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        def r(x: int) -> int:
            new = 0
            while x > 0:
                new = (new << 1) | (x & 1)
                x >>= 1
            return new
        a = [(r(n), n) for n in nums]
        a.sort()
        return [n for _, n in a]


