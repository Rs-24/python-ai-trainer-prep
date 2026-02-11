# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 8 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/koko-eating-bananas/description/

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            return hours <= h
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([1], 1) == 1
    assert sol.minEatingSpeed([1], 2) == 1
    assert sol.minEatingSpeed([1, 2, 3], 3) == 3
    assert sol.minEatingSpeed([1, 2, 3], 4) == 3
    assert sol.minEatingSpeed([3, 2, 5, 8, 1], 5) == 8
    assert sol.minEatingSpeed([3, 2, 5, 8, 1], 6) == 8

# Explanation: the code uses a lower bounded binary search to find the minimum
# value of k, while checking whether the bananas can be eaten within h hours
# with each value of mid
# Time: O(n * log m), n = len(piles), m = max(piles)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 1h 8 mins):
#   - I now realise my tests can be improved, my rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.minEatingSpeed([1], 1) == 1
#     assert sol.minEatingSpeed([1], 2) == 1
#     assert sol.minEatingSpeed([2], 1) == 2
#     assert sol.minEatingSpeed([1, 2, 3], 3) == 3
#     assert sol.minEatingSpeed([1, 2, 3], 4) == 3
#     assert sol.minEatingSpeed([3, 2, 5, 8, 1], 5) == 8
#     assert sol.minEatingSpeed([3, 2, 5, 8, 1], 6) == 8






