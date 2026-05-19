

class Solution:
    def trimMean(self, arr: list) -> float:
        # Time: O(n log n), n = len(arr)
        # Space: O(1)
        arr.sort()
        n = len(arr)
        s = 0
        for i in range(int(n * 0.05), int(n * 0.95)):
            s += arr[i]
        return s / (0.9 * n)


