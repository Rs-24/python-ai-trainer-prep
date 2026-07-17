

class Solution:
    def findLongestChain(self, pairs: list[list]) -> int:
        # Time: O(n log n)
        # Space: O(1)
        pairs.sort(key=lambda x: x[1])
        a, p = 0, float("-inf")
        for l, r in pairs:
            if p < l:
                a += 1
                p = r
        return a


