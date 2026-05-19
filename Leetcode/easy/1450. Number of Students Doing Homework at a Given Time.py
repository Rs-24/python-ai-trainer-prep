


class Solution:
    def busyStudent(self, startTime: list, endTime: list, queryTime: int) -> int:
        # Time: O(n), n = len(startTime) = len(endTime)
        # Space: O(1)
        count = 0
        for s, e in zip(startTime, endTime):
            count += s <= queryTime <= e
        return count


