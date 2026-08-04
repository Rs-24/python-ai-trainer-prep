

class Solution:
    def maxTurbulenceSize(self, arr: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(arr)
        if n == 1:
            return 1
        u = d = a = 1
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                u = d + 1
                d = 1
            elif arr[i - 1] > arr[i]:
                d = u + 1
                u = 1
            else:
                u = d = 1
            a = max(a, u, d)
        return a


