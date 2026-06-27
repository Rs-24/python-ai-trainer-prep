

from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        if target > x + y:
            return False
        if target == 0:
            return True
        return target % gcd(x, y) == 0


