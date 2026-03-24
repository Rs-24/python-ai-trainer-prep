# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/teemo-attacking/description/

from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Time: O(n), n = len(timeSeries)
        # Space: O(1)
        if not timeSeries:
            return 0
        total = 0
        i = 0
        while i < len(timeSeries):
            if i < len(timeSeries) - 1 and timeSeries[i] + duration - 1 >= timeSeries[i + 1]:
                total += (timeSeries[i + 1] - timeSeries[i])
            else:
                total += duration
            i += 1
        return total

# min() method:
from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Time: O(n), n = len(timeSeries)
        # Space: O(1)
        if not timeSeries:
            return 0
        total = 0
        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i - 1])
        total += duration
        return total
   

