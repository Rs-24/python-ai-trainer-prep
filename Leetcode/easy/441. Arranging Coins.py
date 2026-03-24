# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            total = (mid * (mid + 1)) // 2
            if total == n:
                return mid
            elif total < n:
                l = mid + 1
            else:
                r = mid - 1
        return r


