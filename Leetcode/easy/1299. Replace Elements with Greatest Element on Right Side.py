

class Solution:
    def replaceElements(self, arr: list) -> list:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        best = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = best
            best = max(best, temp)
        return arr


