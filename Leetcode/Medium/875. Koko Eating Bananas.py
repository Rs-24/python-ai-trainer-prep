# Time to write all of below including tests, explanation and time and aux
# and total space: 38 mins

# Problem: https://leetcode.com/problems/koko-eating-bananas/description/

from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(x: int) -> bool:
            hours = 0
            for p in piles:
                hours += ((p + x - 1) // x)
            return hours <= h
        def lower_bound(l: int, r: int) -> int:
            while l < r:
                mid = (l + r) // 2
                if can_finish(mid):
                    r = mid
                else:
                    l = mid + 1
            return l
        return lower_bound(1, max(piles))

if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([1], 1) == 1
    assert sol.minEatingSpeed([1], 2) == 1
    assert sol.minEatingSpeed([2], 1) == 2
    assert sol.minEatingSpeed([1, 2, 3], 3) == 3
    assert sol.minEatingSpeed([1, 2, 3], 4) == 3
    assert sol.minEatingSpeed([3, 2, 5, 8, 1], 5) == 8
    assert sol.minEatingSpeed([3, 2, 5, 8, 1], 6) == 8

# Explanation: the code uses a lower bounded binary search to find the minimum
# value of k, while checking whether the bananas can be eaten within h hours
# with each value of mid
# Time: O(n log m), n = len(piles), m = max(piles)
# Space: O(1)


