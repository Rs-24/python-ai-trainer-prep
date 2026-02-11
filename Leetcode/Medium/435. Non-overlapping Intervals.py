# Time to write all of below including tests, explanation and time and aux
# and total space: 58 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if prev_end > a:
                count += 1
                prev_end = min(prev_end, b)
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
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 58 mins):
#   - No major learning lessons




