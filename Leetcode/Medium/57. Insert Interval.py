# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 32 mins

# I required help from chatGPT to solve this one 

# Problem: https://leetcode.com/problems/insert-interval/description/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:                
        out = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1
        start, end = newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        out.append([start, end])
        while i < n:
            out.append(intervals[i])
            i += 1
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.insert([], [1, 2]) == [[1, 2]]
    assert sol.insert([[1, 2], [3, 4]], [2, 3]) == [[1, 4]]
    assert sol.insert([[1, 2], [3, 4]], [2, 2]) == [[1, 2], [3, 4]]
    assert sol.insert([[1, 1], [3, 4]], [2, 3]) == [[1, 1], [2, 4]]
    assert sol.insert([[1, 2], [3, 4]], [5, 6]) == [[1, 2], [3, 4], [5, 6]]
    assert sol.insert([[0, 3], [5, 6]], [0, 4]) == [[0, 4], [5, 6]]

# Explanation: the code first appends all intervals before newInterval to out,
# then merges newInterval with existing intervals or appends it unchanged, and
# then appends all intervals after newInterval
# Time: O(n), n = len(intervals)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(n)
 
# Learning lessons (done after completing all of above in 1h 32 mins):
#   - No major learning lessons




















