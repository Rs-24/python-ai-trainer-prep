# Time to write all of below including tests, explanation and time and aux
# and total space: 2h 12 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/merge-intervals/description/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                merged[-1][1] = max(end, last_end)
            else:
                merged.append([start, end])
        return merged

if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[0, 1]]) == [[0, 1]]
    assert sol.merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert sol.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert sol.merge([[1, 3], [2, 4]]) == [[1, 4]]
    assert sol.merge([[0, 2], [2, 4], [3, 5], [6, 8]]) == [[0, 5], [6, 8]]
    assert sol.merge([[1, 1], [2, 4]]) == [[1, 1], [2, 4]]

# Explanation: the code sorts intervals by start time and creates a new list
# called merged, and iterates through intervals while modifying merged
# Time: O(n + n log n), n = len(intervals)
# Aux space, excluding output and input: O(1), depending on sorting
# implementation, as .sort() may use additional overhead
# Total space, including output, excluding input: O(k), k = number of
# items appended to merged

# Learning lessons (done after completing all of above in 2h 12 mins):
#   - I now realise my aux space comment can be improved. My rewrite is below: 
#
# Aux space, excluding output and input: O(log n), due to overhead from .sort()





