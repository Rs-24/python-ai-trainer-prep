

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        n = len(arr)
        for i in range(n - n // 4):
            if arr[i] == arr[i + n // 4]:
                return arr[i]


