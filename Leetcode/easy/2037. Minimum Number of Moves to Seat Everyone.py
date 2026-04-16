# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Time: O(n log n), n = len(seats) = len(students)
        # Space: O(n)
        seats.sort()
        students.sort()
        total = 0
        for i, seat in enumerate(seats):
            total += abs(students[i] - seat)
        return total


