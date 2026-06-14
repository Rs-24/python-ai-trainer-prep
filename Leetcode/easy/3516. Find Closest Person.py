

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Time: O(1)
        # Space: O(1)
        a = abs(x - z)
        b = abs(y - z)
        if a < b:
            return 1
        if a > b:
            return 2
        return 0


