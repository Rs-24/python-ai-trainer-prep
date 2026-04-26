# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/total-distance-traveled/description/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return 10 * (mainTank + min(((mainTank - 1) // 4), additionalTank))


