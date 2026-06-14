

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # Time: O(n^2)
        # Space: O(n)
        return [sum(r) for r in matrix]


