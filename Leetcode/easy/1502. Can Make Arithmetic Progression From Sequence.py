

class Solution:
    def canMakeArithmeticProgression(self, arr: list) -> bool:
        # Time: O(n log n), n = len(arr)
        # Space: O(1)
        arr.sort()
        prev = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != prev:
                return False
        return True


