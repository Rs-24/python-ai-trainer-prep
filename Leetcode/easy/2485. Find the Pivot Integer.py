# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-pivot-integer/description/

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        total = (n * (n + 1)) // 2
        x = int(total ** 0.5)
        return x if x * x == total else -1


