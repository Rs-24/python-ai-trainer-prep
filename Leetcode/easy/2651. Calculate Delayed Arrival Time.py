# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/calculate-delayed-arrival-time/description/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (arrivalTime + delayedTime) % 24


