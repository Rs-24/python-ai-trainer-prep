

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(1)
        if sum(arr) % 3 != 0:
            return False
        t = sum(arr) // 3
        cur = 0
        parts = 0
        for num in arr:
            cur += num
            if cur == t:
                parts += 1
                cur = 0
        return parts >= 3


