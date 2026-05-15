

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        n = len(arr)
        z = arr.count(0)
        i = n - 1
        j = n - 1 + z
        while i >= 0:
            if arr[i] == 0:
                j -= 1
            if j < n:
                arr[j] = arr[i]
            i -= 1
            j -= 1


