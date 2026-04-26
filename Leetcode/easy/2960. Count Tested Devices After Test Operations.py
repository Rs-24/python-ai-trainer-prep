# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-tested-devices-after-test-operations/description/

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        # Time: O(n), n = len(batteryPercentages)
        # Space: O(1)
        count = 0
        for b in batteryPercentages:
            if b > count:
                count += 1
        return count


