# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-closest-person/description/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Time: O(1)
        # Space: O(1)
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        if d1 > d2:
            return 2
        return 0


