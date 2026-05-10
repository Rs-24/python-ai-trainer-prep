# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/button-with-longest-push-time/description/

from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # Time: O(n), n = len(events)
        # Space: O(1)
        longest_time = events[0][1]
        corresponding_index = events[0][0]
        prev_time = 0
        for a, b in events:
            if b - prev_time > longest_time or (b - prev_time == longest_time and a < corresponding_index):
                longest_time = b - prev_time
                corresponding_index = a
            prev_time = b
        return corresponding_index


