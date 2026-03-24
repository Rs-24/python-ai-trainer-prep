# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/construct-the-rectangle/description/

from typing import List
from math import sqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Time: O(n), n = sqrt(area)
        # Space, excluding output: O(1)
        x = int(sqrt(area))
        while area % x != 0:
            x -= 1
        return [area // x, x]


