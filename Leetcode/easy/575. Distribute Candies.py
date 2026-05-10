

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        # Time: O(n), n = len(candyType)
        # Space: O(n)
        return min(len(candyType) // 2, len(set(candyType)))


