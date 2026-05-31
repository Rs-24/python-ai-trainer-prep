

from collections import deque

class Solution:
    def lastVisitedIntegers(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        seen = deque()
        ans = []
        k = 0
        for num in nums:
            if num > 0:
                seen.appendleft(num)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans


