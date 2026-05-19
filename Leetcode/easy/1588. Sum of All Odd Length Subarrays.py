

class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        s = 0
        n = len(arr)
        for i, num in enumerate(arr):
            total = (i + 1) * (n - i)
            odd = (total + 1) // 2
            s += num * odd
        return s


