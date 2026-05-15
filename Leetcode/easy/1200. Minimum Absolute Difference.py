

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        arr.sort()
        best = float("inf")
        out = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < best:
                out = [[arr[i], arr[i + 1]]]
                best = arr[i + 1] - arr[i]
            elif arr[i + 1] - arr[i] == best:
                out.append([arr[i], arr[i + 1]])
        return out


