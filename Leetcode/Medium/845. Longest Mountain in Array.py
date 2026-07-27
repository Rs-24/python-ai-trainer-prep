

class Solution:
    def longestMountain(self, arr: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(arr)
        i = a = 0
        while i < n:
            j = i
            while j < n - 1 and arr[j] < arr[j + 1]:
                j += 1
            if j == i or j == n - 1:
                i += 1
                continue
            j += 1
            t = j
            while j < n - 1 and arr[j] > arr[j + 1]:
                j += 1
            if t == j:
                i += 1
                continue
            a = max(a, j - i + 1)
            i = j
        return a


