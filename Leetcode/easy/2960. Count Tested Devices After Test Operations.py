

class Solution:
    def countTestedDevices(self, batteryPercentages: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c = 0
        for b in batteryPercentages:
            c += 1 if b > c else 0
        return c


