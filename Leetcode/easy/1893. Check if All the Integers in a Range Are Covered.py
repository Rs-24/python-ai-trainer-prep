

class Solution:
    def isCovered(self, ranges: list[list], left: int, right: int) -> bool:
        # Time: O(n), n = len(ranges)
        # Space: O(1)
        arr = [False] * 52
        for a, b in ranges:
            for i in range(a, b + 1):
                arr[i] = True
        return all(arr[i] for i in range(left, right + 1))


