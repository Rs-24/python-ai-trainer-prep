

class Solution:
    def peakIndexInMountainArray(self, arr: list) -> int:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l


        