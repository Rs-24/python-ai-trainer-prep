

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        # Time: O(n * k + n log n)
        # Space: O(n)
        if len(nums) % k != 0:
            return False
        c = Counter(nums)
        for num in sorted(c):
            t = c[num]
            if t == 0:
                continue
            for nxt in range(num, num + k):
                if c[nxt] < t:
                    return False
                c[nxt] -= t
        return True


