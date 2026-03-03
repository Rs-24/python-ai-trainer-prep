# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/merge-intervals/description/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = []
        prev_a, prev_b = intervals[0]
        for a, b in intervals[1:]:
            if a <= prev_b:
                prev_b = max(prev_b, b)
            else:
                out.append([prev_a, prev_b])
                prev_a, prev_b = a, b
        out.append([prev_a, prev_b])
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[0, 1]]) == [[0, 1]]
    assert sol.merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert sol.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert sol.merge([[1, 3], [2, 4]]) == [[1, 4]]
    assert sol.merge([[0, 2], [2, 4], [3, 5], [6, 8]]) == [[0, 5], [6, 8]]
    assert sol.merge([[1, 1], [2, 4]]) == [[1, 1], [2, 4]]

# Explanation: the code sorts intervals by start time and creates a new list
# called out, and appends the sorted intervals while merging the relevant
# intervals
# Time: O(n log n), n = len(intervals)
# Space: excluding output: worst case O(n) due to .sort()       


