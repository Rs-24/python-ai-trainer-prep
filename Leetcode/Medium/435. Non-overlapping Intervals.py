# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if prev_end > a:
                prev_end = min(prev_end, b)
                count += 1
            else:
                prev_end = b
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2]]) == 0
    assert sol.eraseOverlapIntervals([[-1, 0], [0, 1], [-1, 1]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 3], [2, 4], [2, 3]]) == 2
    
# Explanation: the code sorts the intervals by start time ascending, and if
# any intervals overlap, increments count and keeps the interval with the 
# earliest end
# Time: O(n log n), n = len(intervals)
# Space: worst case O(n) depending on sorting implementation of .sort()


