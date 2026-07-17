

class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        # Time: O(log n)
        # Space: O(k)
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]


        