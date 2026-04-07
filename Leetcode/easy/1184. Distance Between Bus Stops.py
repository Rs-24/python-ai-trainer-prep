# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/distance-between-bus-stops/description/

from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Time: O(n), n = len(distance)
        # Space: O(n)
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        anticlockwise = sum(distance) - clockwise
        return min(clockwise, anticlockwise)


