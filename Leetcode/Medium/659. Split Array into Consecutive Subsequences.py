

from collections import Counter

class Solution:
    def isPossible(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        t = Counter()
        for x in nums:
            if c[x] == 0:
                continue
            c[x] -= 1
            if t[x] > 0:
                t[x] -= 1
                t[x + 1] += 1
            elif c[x + 1] > 0 and c[x + 2] > 0:
                c[x + 1] -= 1
                c[x + 2] -= 1
                t[x + 3] += 1
            else:
                return False
        return True


