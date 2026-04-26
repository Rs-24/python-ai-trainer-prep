# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/convert-the-temperature/description/

from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Time: O(1)
        # Space: O(1)
        return [celsius + 273.15, celsius * 1.8 + 32]


