

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return 10 * (mainTank + min((mainTank - 1) // 5, additionalTank))


