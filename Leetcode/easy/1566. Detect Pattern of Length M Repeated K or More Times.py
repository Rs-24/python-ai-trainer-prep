

class Solution:
    def containsPattern(self, arr: list, m: int, k: int) -> bool:
        # Time: O(n - m), n = len(arr)
        # Space: O(1)
        count = 0
        for i in range(m, len(arr)):
            if arr[i] == arr[i - m]:
                count += 1
                if count == m * (k - 1):
                    return True
            else:
                count = 0
        return False
            

