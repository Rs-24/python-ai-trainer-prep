# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # Time: O(n), n = len(startTime) = len(endTime)
        # Space: O(1)
        total = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                total += 1
        return total


