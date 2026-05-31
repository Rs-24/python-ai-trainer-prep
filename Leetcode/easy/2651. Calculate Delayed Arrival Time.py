

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (arrivalTime + delayedTime) % 24


