

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # Time: O(n log n), n = len(heights)
        # Space: O(n)
        return sum(h != s for h, s in zip(heights, sorted(heights)))


